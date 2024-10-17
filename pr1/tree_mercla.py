import hashlib
from find_nonce import find_nonce

class TreeMercla:
    nodes: list[str]
    n: int
    low_level_i: int
    lvl_count: int
    sheet_count: int

    neitral: str

    def __init__(self, transaction: list[str]):
        n = len(transaction)
        need_n = 1
        self.lvl_count = 1

        while need_n < n:
            need_n *= 2
            self.lvl_count += 1

        n = need_n
        need_n *= 2

        self.n = need_n - 1
        self.low_level_i = (need_n // 2) - 1

        self.nodes = [None] * (need_n - 1)

        it = 0
        for i in range(self.low_level_i, need_n - 1):
            self.nodes[i] = hashlib.sha256(transaction[it].encode()).hexdigest()
            it += 1

            if len(transaction) <= it:
                it -= 1
                self.neitral = hashlib.sha256(transaction[it].encode()).hexdigest()
                break
        
        self.sheet_count = len(transaction)
        self._tree_calculate()
    
    def _tree_calculate(self, v:int = 0) -> str:
        if v >= self.low_level_i:
            return self.nodes[v]

        a = self._tree_calculate(v * 2 + 1)
        b = self._tree_calculate(v * 2 + 2)

        if (a == b and a == None):
            self.sheet_count += 1
            a = self.neitral
            b = self.neitral

        elif a == None:
            self.sheet_count += 1
            a = self.neitral
        
        elif b == None:
            self.sheet_count += 1
            b = self.neitral
            

        self.nodes[v] = hashlib.sha256((a + b).encode()).hexdigest()
        return self.nodes[v]

    def get_root(self) -> str:
        return self.nodes[0]
    
    def get_level(self) -> int:
        return self.lvl_count
    
    def get_sheet(self) -> int:
        return self.sheet_count

def main():
    tree = TreeMercla(["abc", "5+5", "2*2", "666", "777"])
    print(tree.get_root())
    print(f"level: {tree.get_level()}")
    print(f"sheet: {tree.get_sheet()}")

if __name__ == "__main__":
    main()