class Question:
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, test_row):
        test_val = test_row[self.column]

        if self.is_numeric(test_val):
            return test_val >= self.value

        return test_val == self.value

    def print(self, header_):
        condition = "=="
        if self.is_numeric(self.value):
            condition = ">="
        return "Is %s %s %s?" % (header_[self.column], condition, str(self.value))

    @staticmethod
    def is_numeric(value):
        return isinstance(value, int) or isinstance(value, float)


class Leaf:
    def __init__(self, rows):
        self.predictions = class_counts(rows)


class DecisionNode:
    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch


def class_counts(rows):
    counts = {}
    for row in rows:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


class DecisionTree:
    def __init__(self, training_data):
        self.root_node = self._build_tree(training_data)

    def _build_tree(self, rows):
        info, question = self._find_best_split(rows)
        if info == 0:
            return Leaf(rows)

        true_rows, false_rows = self._partition(rows, question)
        true_branch = self._build_tree(true_rows)
        false_branch = self._build_tree(false_rows)

        return DecisionNode(question, true_branch, false_branch)

    def _find_best_split(self, rows):
        best_gain = 0
        best_question = None
        current_uncertainty = self._gini_impurity(rows)
        n_features = len(rows[0]) - 1

        for col in range(n_features):
            values = set([row[col] for row in rows])
            for val in values:
                question = Question(col, val)
                true_rows, false_rows = self._partition(rows, question)

                if len(true_rows) == 0 or len(false_rows) == 0:
                    continue

                gain = self._info_gain(true_rows, false_rows, current_uncertainty)

                if gain >= best_gain:
                    best_gain, best_question = gain, question

        return best_gain, best_question

    def _info_gain(self, left, right, current_uncertainty):
        p = float(len(left)) / (len(left) + len(right))
        return current_uncertainty - p * self._gini_impurity(left) - (1 - p) * self._gini_impurity(right)

    def classify(self, row):
        return self._classify(row, self.root_node)

    def _classify(self, row, node):
        if isinstance(node, Leaf):
            return node.predictions

        return self._classify(row, node.true_branch) if node.question.match(row) \
            else self._classify(row, node.false_branch)

    @staticmethod
    def print_predictions(predictions):
        total = sum(predictions.values()) * 1.0
        probs = {}
        for lbl in predictions.keys():
            probs[lbl] = str(int(predictions[lbl] / total * 100)) + "%"
        return probs

    def print_tree(self):
        self._print_node(self.root_node)

    def _print_node(self, node, spacing=""):
        if isinstance(node, Leaf):
            print(spacing + "Predict", node.predictions)
            return

        # Print the question at this node
        print (spacing + node.question.print(header))

        # Call this function recursively on the true branch
        print (spacing + '--> True:')
        self._print_node(node.true_branch, spacing + "  ")

        # Call this function recursively on the false branch
        print (spacing + '--> False:')
        self._print_node(node.false_branch, spacing + "  ")

    @staticmethod
    def _gini_impurity(rows):
        counts = class_counts(rows)
        impurity = 1
        for label in counts:
            prob_of_label = counts[label] / float(len(rows))
            impurity -= prob_of_label ** 2
        return impurity

    @staticmethod
    def _partition(rows, question):
        true_rows, false_rows = [], []
        for row in rows:
            true_rows.append(row) if question.match(row) else false_rows.append(row)
        return true_rows, false_rows


training_data_example = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

testing_data_example = [
    ['Green', 3, 'Apple'],
    ['Yellow', 4, 'Apple'],
    ['Red', 2, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

header = ["color", "diameter", "label"]

if __name__ == '__main__':
    decision_tree = DecisionTree(training_data_example)
    decision_tree.print_tree()

    for entry in testing_data_example:
        print("Actual: %s. Predicted: %s " % (entry[-1], decision_tree.print_predictions(decision_tree.classify(entry))))


