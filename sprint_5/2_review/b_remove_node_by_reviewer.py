"""
Получилась хорошая эффективная реализация!
У нее есть один недостаток - она довольно запутанная. Если подобная задача
попадется где-нибудь на алгособесе, то шансы реализовать ее в таком виде
небольшие. Существует очень лаконичная рекурсивная реализация, идею которой
рекомендую запомнить и в случае чего воспользоваться :)
"""


def remove(self, root: Optional[Node], key: int) -> Optional[Node]:
    if not root:
        return None

    if root.value == key:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        replace_by = root.left
        while replace_by.right is not None:
            replace_by = replace_by.right

        root.value = replace_by.value
        root.left = self.remove(root.left, replace_by.value)
        return root

    if key < root.value:
        root.left = self.remove(root.left, key)
    else:
        root.right = self.remove(root.right, key)

    return root
