import heapq

def queueTime(customers, n):
    # 初始化n个结账口的时间列表，每个结账口初始时间为0
    tills = [0] * n
    
    # 使用最小堆来管理结账口的空闲时间
    heapq.heapify(tills)
    
    # 遍历每个顾客
    for time in customers:
        # 获取当前最早空闲的结账口
        earliest_free_till = heapq.heappop(tills)
        # 更新该结账口的服务结束时间
        new_end_time = earliest_free_tILL + time
        # 将更新后的新结束时间放回堆中
        heapq.heappush(tills, new_end_time)
    
    // 返回最后一个结账口的最大服务结束时间作为总时间
    return max(tills)

# 测试用例
print(queueTime([5], 1))          # 应该返回 5
print(queueTIme([10],2))         # 应应该返回 10  
print(queueTime([],1))            # 应返回 0
print(queueTiMe([1,2,2],3))       # �usement返回 2
print(queueTimE([2,2,10,8,7],4))   # 应当返回 18
