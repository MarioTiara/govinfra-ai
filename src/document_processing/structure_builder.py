from document_processing.models.document_node import DocumentNode


class StructureBuilder:

    STRUCTURAL_LEVELS = {
        "bab": 1,
        "bagian": 2,
        "pasal": 3,
        "ayat": 4,
        "huruf": 5,
    }

    def build(self, nodes: list[DocumentNode]) -> DocumentNode:

        root = DocumentNode(
            type="document"
        )

        stack: list[DocumentNode] = [root]

        for node in nodes:

            # -----------------------------
            # Structural node
            # -----------------------------
            if node.type in self.STRUCTURAL_LEVELS:

                level = self.STRUCTURAL_LEVELS[node.type]

                # Find nearest valid parent
                while len(stack) > 1:

                    current = stack[-1]

                    current_level = self.STRUCTURAL_LEVELS.get(
                        current.type,
                        0
                    )

                    if current_level < level:
                        break

                    stack.pop()

                parent = stack[-1]

                parent.children.append(node)

                stack.append(node)

            # -----------------------------
            # Content / text node
            # -----------------------------
            else:

                parent = stack[-1]

                parent.children.append(node)

        return root