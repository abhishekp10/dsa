
"""
Attempt to design a cache with following rules
#1 if expired itemp is available, remove it (if multiple with same expiry remove anyone)
#2 if nothing expired, remove one with least priority
#3 if more than one with #2, remove the least recently used

Solution using double linked list and hashmap

"""

from datetime import datetime
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self,start,end):
        self.head=Node(0,start)
        self.tail=Node(0,end) 
        self.head.next=self.tail
        self.tail.prev=self.head  

    def sorted_insert(self,new_node):      
        current =self.head

        while ((current.next is not self.tail) and (current.next.value <= new_node.value)):
            current = current.next

        new_node.next = current.next

        #if current.next is not self.tail:
        new_node.next.prev = new_node
        
        current.next =new_node
        new_node.prev=current
    
    def left_insert(self,new_node):
        
        prev_end = self.head.next
        prev_end.prev = new_node
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = prev_end


    def delete_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def printList(self):
  
        node = self.head.next
        while node and node is not self.tail:
            print([str(node.value),str(node.key)])
            node = node.next

    def find_min_node(self):
        min_node = self.head.next
        return min_node     

class LRU:
    def __init__(self,capacity):
        self.capacity = capacity
        self.hm_p={}
        self.hm_l={}
        self.hm_e={}
        self.priority_list = DoublyLinkedList(-999,999)
        self.expiry_list = DoublyLinkedList('1970-01-01','2100-01-01')
        self.lru_list = DoublyLinkedList(0,0)
    
    def put(self,key,value, pr, exp):
        if key in self.hm_p:
            node_p,node_l,node_e = self.hm_p[key],self.hm_l[key],self.hm_e[key]
            self.lru_list.delete_node(node_l) 
            self.expiry_list.delete_node(node_e) 
            self.priority_list.delete_node(node_p) 
            del self.hm_p[key],self.hm_l[key],self.hm_e[key]

        node_p,node_l,node_e=Node(key,pr),Node(key,value),Node(key,exp)
        self.lru_list.left_insert(node_l) 
        self.expiry_list.sorted_insert(node_e) 
        self.priority_list.sorted_insert(node_p) 
        self.hm_p[key],self.hm_l[key],self.hm_e[key]=node_p,node_l,node_e

        if len(self.hm_l) > self.capacity:
            expired_node=self.expiry_list.find_min_node()
            low_priority_node=self.priority_list.find_min_node()
            next_low_priority_node=low_priority_node.next
            lru_node=self.lru_list.tail.prev
            #print('todays date',datetime.now().strftime('%Y-%m-%d'))
            if expired_node.value <= datetime.now().strftime('%Y-%m-%d'):
                #print('type',type(expired_node.value),datetime.now().strftime('%Y-%m-%d'))
                self.lru_list.delete_node(self.hm_l[expired_node.key]) 
                self.expiry_list.delete_node(expired_node) 
                self.priority_list.delete_node(self.hm_p[expired_node.key]) 
                del self.hm_p[expired_node.key],self.hm_l[expired_node.key],self.hm_e[expired_node.key]
            elif low_priority_node.value <= 2:
                if next_low_priority_node.value == low_priority_node.value:
                    if next_low_priority_node.key == lru_node.key:
                        node_to_delete = next_low_priority_node
                    else:
                        node_to_delete = low_priority_node
                    self.lru_list.delete_node(self.hm_l[node_to_delete.key]) 
                    self.expiry_list.delete_node(node_to_delete) 
                    self.priority_list.delete_node(self.hm_p[node_to_delete.key]) 
                    del self.hm_p[node_to_delete.key],self.hm_l[node_to_delete.key],self.hm_e[node_to_delete.key]
        
        self.lru_list.printList()
        self.priority_list.printList()
        self.expiry_list.printList()


    def get(self,key):
        if key not in self.hm_l:
            return
        node_to_update = self.hm_l[key] 
        self.lru_list.delete_node(node_to_update)
        self.lru_list.left_insert(node_to_update)
        return node_to_update.value

        
    

LRU_Cache=LRU(2)
LRU_Cache.put(1,1,5,'2023-07-03')
print(LRU_Cache.get(1))
LRU_Cache.put(2,2,1,'2022-01-02')
LRU_Cache.put(3,3,1,'2024-01-02')
LRU_Cache.put(4,4,1,'2024-03-02')
print(LRU_Cache.get(4))


