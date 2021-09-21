from tree_sitter import Language, Parser

PY_LANGUAGE = Language('my-languages.so', 'python')
parser = Parser()
parser.set_language(PY_LANGUAGE)

# 判定节点字典
judge_dict = {
    "for_statement": 1,
    "if_statement": 1,
    "elif_clause": 1,
    "while_statement": 1,
    "and": 1,
    "or": 1,
}


# 判断是不是一个判定节点
def judge(node, numb):
    if node.type in judge_dict:
        numb += 1
    return numb


# 前序遍历ast 查找判定节点
def get_cyclic_complexity(cursor, move, numb):
    if move == "down":
        numb = judge(cursor.node, numb)
        if cursor.goto_first_child():
            numb = get_cyclic_complexity(cursor, "down", numb)
        elif cursor.goto_next_sibling():
            numb = get_cyclic_complexity(cursor, "right", numb)
        elif cursor.goto_parent():
            numb = get_cyclic_complexity(cursor, "up", numb)
    elif move == "right":
        numb = judge(cursor.node, numb)
        if cursor.goto_first_child():
            numb = get_cyclic_complexity(cursor, "down", numb)
        elif cursor.goto_next_sibling():
            numb = get_cyclic_complexity(cursor, "right", numb)
        elif cursor.goto_parent():
            numb = get_cyclic_complexity(cursor, "up", numb)
    elif move == "up":
        if cursor.goto_next_sibling():
            numb = get_cyclic_complexity(cursor, "right", numb)
        elif cursor.goto_parent():
            numb = get_cyclic_complexity(cursor, "up", numb)
    return numb


def compute(code_str):
    tree = parser.parse(bytes(code_str, 'utf8'))
    cursor = tree.walk()
    base = 1
    cyclic = get_cyclic_complexity(cursor, "down", base)
    return cyclic
