"""Tests for the Code Jam 12 Qualifier Challenge."""

import unittest

import qualifier
from node import Node

solution = qualifier.query_selector_all


class TestQuerySelector(unittest.TestCase):
    """Test cases for the query_selector_all function."""

    def setUp(self) -> None:
        """Set up a sample Node tree for testing."""
        self.node_test1 = Node(
            tag="div",
            attributes={"id": "topDiv"},
            children=[
                Node(
                    tag="div",
                    attributes={"id": "innerDiv", "class": "container colour-primary"},
                    children=[
                        Node(tag="h1", text="This is a heading!"),
                        Node(
                            tag="p",
                            attributes={"class": "colour-secondary", "id": "innerContent"},
                            text="I have some content within this container also!",
                        ),
                        Node(
                            tag="p",
                            attributes={"class": "colour-secondary", "id": "two"},
                            text="This is another paragraph.",
                        ),
                        Node(
                            tag="p",
                            attributes={"class": "colour-secondary important"},
                            text="This is a third paragraph.",
                        ),
                        Node(
                            tag="a",
                            attributes={"id": "home-link", "class": "colour-primary button"},
                            text="This is a button link.",
                        ),
                    ],
                ),
                Node(
                    tag="div",
                    attributes={"class": "container colour-secondary"},
                    children=[
                        Node(
                            tag="p",
                            attributes={"class": "colour-primary"},
                            text="This is a paragraph in a secondary container.",
                        ),
                    ],
                ),
            ],
        )

    def test_tag(self) -> None:
        """Test basic tag selector."""
        node = self.node_test1
        result = solution(node, "div")
        answer = [node, node.children[0], node.children[1]]
        assert result == answer

    def test_id(self) -> None:
        """Test ID selector."""
        node = self.node_test1
        result = solution(node, "#innerDiv")
        answer = [node.children[0]]
        assert result == answer

    def test_class(self) -> None:
        """Test class selector."""
        node = self.node_test1
        result = solution(node, ".colour-primary")
        answer = [node.children[0], node.children[0].children[4], node.children[1].children[0]]
        assert result == answer

    # Test compound selector
    def test_tag_class(self) -> None:
        """Test tag and class selector."""
        node = self.node_test1
        result = solution(node, "p.colour-secondary")
        answer = [node.children[0].children[1], node.children[0].children[2], node.children[0].children[3]]
        assert result == answer

    def test_tag_id(self) -> None:
        """Test tag and ID selector."""
        node = self.node_test1
        result = solution(node, "div#innerDiv")
        answer = [node.children[0]]
        assert result == answer

    def test_id_class(self) -> None:
        """Test ID and class selector."""
        node = self.node_test1
        result = solution(node, "#innerContent.colour-secondary")
        answer = [node.children[0].children[1]]
        assert result == answer

    def test_tag_id_class(self) -> None:
        """Test tag, ID, and class selector."""
        node = self.node_test1
        result = solution(node, "div#innerDiv.colour-primary")
        answer = [node.children[0]]
        assert result == answer

    def test_multi_class(self) -> None:
        """Test multiple classes selector."""
        node = self.node_test1
        result = solution(node, ".colour-primary.button")
        answer = [node.children[0].children[4]]
        assert result == answer

    def test_tag_multi_class(self) -> None:
        """Test tag with multiple classes selector."""
        node = self.node_test1
        result = solution(node, "#home-link.colour-primary.button")
        answer = [node.children[0].children[4]]
        assert result == answer

    def test_tag_id_multi_class(self) -> None:
        """Test tag, ID, and multiple classes selector."""
        node = self.node_test1
        result = solution(node, "a#home-link.colour-primary.button")
        answer = [node.children[0].children[4]]
        assert result == answer

    # Test multiple selectors
    def test_multi_selector(self) -> None:
        """Test multiple selectors separated by commas."""
        node = self.node_test1
        result = solution(node, "#topDiv, h1, .colour-primary")
        answer = [
            node, node.children[0], node.children[0].children[0],
            node.children[0].children[4], node.children[1].children[0],
        ]
        assert result == answer

    def test_multi_selector_compound(self) -> None:
        """Test multiple compound selectors."""
        node = self.node_test1
        result = solution(node, "h1, a#home-link.colour-primary.button")
        answer = [node.children[0].children[0], node.children[0].children[4]]
        assert result == answer

    def test_compound_multi_selector_compound(self) -> None:
        """Test multiple compound selectors with different combinations."""
        node = self.node_test1
        result = solution(node, "p#two.colour-secondary, a#home-link.colour-primary.button")
        answer = [node.children[0].children[2], node.children[0].children[4]]
        assert result == answer

    # Test absence
    def test_absent_tag(self) -> None:
        """Test absent tag selector."""
        node = self.node_test1
        result = solution(node, "i")
        answer = []
        assert result == answer

    def test_absent_id(self) -> None:
        """Test absent ID selector."""
        node = self.node_test1
        result = solution(node, "#badID")
        answer = []
        assert result == answer

    def test_absent_class(self) -> None:
        """Test absent class selector."""
        node = self.node_test1
        result = solution(node, ".missing-class")
        answer = []
        assert result == answer

    def test_multi_absent(self) -> None:
        """Test multiple absent selectors."""
        node = self.node_test1
        result = solution(node, "i, #badID, .missing-class")
        answer = []
        assert result == answer

    def test_mixed_absent(self) -> None:
        """Test mixed present and absent selectors."""
        node = self.node_test1
        result = solution(node, "h1, #badID, .missing-class")
        answer = [node.children[0].children[0]]
        assert result == answer

    def test_mixed_absent_compound(self) -> None:
        """Test mixed present and absent compound selectors."""
        node = self.node_test1
        result = solution(node, "li#random.someclass, a#home-link, div, .colour-primary.badclass")
        answer = [node, node.children[0], node.children[0].children[4], node.children[1]]
        assert result == answer


if __name__ == "__main__":
    unittest.main()
