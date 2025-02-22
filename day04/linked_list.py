# 연결 리스트(linked list) - 단방향 연결 리스트
# 각각의 요소(노드)가 데이터(값)과 함께
# 다음 노드를 가리키는 주소값을 가지고 있어서
# 다음 노드로의 이동과 추가, 삭제, 삽입이 빠른 자료구조다.

# 노드
# 데이터와 다음 노드의 주소를 담는 기능을 가진 클래스 선언
class Node:
    # 객체화를 하면서 전달받은 data를 self.data에 대입
    def __init__(self,data):
        self.data=data
        self.next = None  # 다음 노드의 주소값을 가리키는 참조변수
    def __str__(self):
        return str(self.data)
    
# 연결 리스트 클래스를 구현
class Linked_list():
    def __init__(self):
        self.head: Node = None
    
    # 주요 연산 구현
    # 삽입
    # 새로운 노드를 리스트에 추가(선택: 특정 노드 뒤에 삽입)
    def insertion(self,node:Node):
        # 만약 self.head가 없다면
        if not self.head:
            self.head=node
        else:
            # 헤드가 있다면 마지막 노드의 next로 node를 삽입
            self.get_last_node().next =node # 뒤에서 head가 없는 경우를 걸렀기 때문에            
        pass

    # 삭제
    # 특정 노드를 리스트에서 삭제
    # 특정 data를 가지고 있으면 삭제
    # return 삭제된 객체 주소 반환
    def delete(self,data):
        # before는 목표 이전 노드
        # target는 목표 노드
        before,target=self.search(data)
        # 만약 전달받은 data를 가진 노드 객체를 찾았다면
        if before and target:
            # 이전 노드의 next에 목표 노드의 next를 대입
            before.next=target.next
            # 찾은 목표 노드를 반환
            return target
        # 만약 before가 없고, target이 있다면
        # target이 즉 self.head라는 의미이므로
        # 둘이 같은지 확인한 뒤
        elif target is self.head:
            # 같다면 self.head를 None으로 수정
            self.head=None
            # 그리고 self.head였던 target을 반환
            return target
        else: # data를 가진 노드 객체를 못찾았다면
            return None
        
    # 탐색1
    # 특정 데이터를 가진 노드 객체(주소값)를 반환
    def search(self,data):
        # 무한반복으로 node를 가져와서 data를 검사 후
        # 불일치하면 next 객체를 가지고 와서 다시 검사
        # next가 None이면 데이터를 찾지못하는 것이므로 return None
        # 만약 data를 찾았다면 그 즉시 해당 노드 객체 반환
        result =None # 반환할 노드 객체
        # 첫 시작은 self.head로 시작  
        node =self.head
        
        # 현재 node가 있다면 무한반복
        while node:
            # 현재 node의 데이터가 전달받은 데이터와 같다면
            if node.data == data:
                # 현재 node를 result 변수에 담는다.
                result= node
                break
            else:
                # 만약에 node.data가 data와 불일치하면
                # 다음 노드(객체 혹은 None)를 node 변수에 담는다.
                node= node.next
        # data를 가진 node를 찾았다면 node가 result에 담겨있을 것이다.
        # 하지만 data를 가진 node를 마지막 노드를 검사했을때까지
        # 찾지 못했다면 None을 반환할 것이다.
        return result

    # 탐색2
    # next를 가지지 않은 마지막 노드를 반환
    # 재귀함수
    # 조건을 만족할 때까지 자기자신을 호출하여
    # 로직을 수행하는 함수
    def get_last_node(self,node:Node=None):
        # 전달받은 Node객체가 없다면
        if not node:
            # self.head가 있는지 검사
            if self.head:
                # 있다면 node에 self.head를 탐색의 시작지점으로 설정
                return self.get_last_node(self.head)
            else:
                return None 
        else: # 전달된 Node 객체가 있다면
            if node.next: 
                # 전달된 node의 다음 객체를 탐색의 시작지점으로 하여
                # 재귀적으로 함수 호출
                return self.get_last_node(node.next)
            else: # 전달된 node에 next가 없다면 node를 반환
                return node

    # 순회
    # 모든 노드를 방문하여 그 데이터들을 리스트에 담아 반환한다.
    def traverse(self):
        result = list()
        node=self.head
        while node:
            result.append(node.data)
            node=node.next
        return result
    
    def __str__(self):
        return str(self.traverse())
        
if __name__=="__main__":
    # 연결 리스트 선언
    link=Linked_list()

    # 연결 리스트에 넣을 노드 선언
    node1= Node("홍길동")
    node2= Node(30)
    node3= Node("개발자")
    link.insertion(node1)
    link.insertion(node2)
    link.insertion(node3)
    print(link.head.data) # 홍길동
    # 마지막 노드 반환
    print(link.get_last_node().data) # 개발자
    print(link)

    # 데이터 삽입
    [link.insertion(Node(e))for e in range(10)]
    print(link)

    # 데이터 삭제
    link.delete(30)
    print(link)

    _,result=link.search(9)
    print(result)