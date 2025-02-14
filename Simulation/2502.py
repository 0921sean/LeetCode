from collections import defaultdict

class Allocator:

    def __init__(self, n: int):
        self.mem = [-1] * n
        self.blocks = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        for i in range(len(self.mem)):
            if self.mem[i] == -1:
                cnt += 1
            else:
                cnt = 0
            if cnt == size:
                self.mem[i+1-cnt:i+1] = [mID] * cnt
                self.blocks[mID].extend(list(range(i+1-cnt, i+1)))
                # print(self.blocks)
                return i+1-cnt
        return -1

    def freeMemory(self, mID: int) -> int:
        r = len(self.blocks[mID])
        for i in self.blocks[mID]:
            self.mem[i] = -1
        self.blocks[mID] = []
        return r


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)

# Solution 클래스 인스턴스 생성 및 함수 호출
if __name__ == "__main__":
    input1_list = [["Allocator","allocate","allocate","allocate","freeMemory","allocate","allocate","allocate","freeMemory","allocate","freeMemory"]]
    input2_list = [[[10],[1,1],[1,2],[1,3],[2],[3,4],[1,1],[1,1],[1],[10,2],[7]]]
    
    for input1, input2 in zip(input1_list, input2_list):
        allocator = None  # Allocator 객체 초기화
        results = []  # 결과 저장 리스트
        
        for command, params in zip(input1, input2):
            if command == "Allocator":
                allocator = Allocator(*params)
                results.append(None)  # 객체 생성은 반환값 없음
            elif command == "allocate":
                results.append(allocator.allocate(*params))
            elif command == "freeMemory":
                results.append(allocator.freeMemory(*params))

        print(results)