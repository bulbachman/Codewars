# My Solution
# class PaginationHelper:
#
#     # The constructor takes in an array of items and an integer indicating
#     # how many items fit within a single page
#     def __init__(self, collection, items_per_page):
#         self.collection = collection
#         self.items = items_per_page
#         self.pages = 0
#
#     # returns the number of items within the entire collection
#     def item_count(self):
#         return len(self.collection)
#
#     # returns the number of pages
#     def page_count(self):
#         if len(self.collection) % self.items == 0:
#             self.pages = len(self.collection) / self.items
#             return self.pages
#         else:
#             self.pages = int(str((len(self.collection) / self.items))[0]) + 1
#             return self.pages
#
#         # returns the number of items on the given page. page_index is zero based
#         # this method should return -1 for page_index values that are out of range
#
#     def page_item_count(self, page_index):
#         page_index += 1
#         if page_index > self.pages or page_index - 1  < 0:
#             return -1
#         else:
#             if page_index == self.pages:
#                 number_of_elements = len(self.collection) - self.items * (self.pages - 1)
#             else:
#                 number_of_elements = self.items
#         return number_of_elements
#
#         # determines what page an item at the given index is on. Zero based indexes.
#         # this method should return -1 for item_index values that are out of range
#
#     def page_index(self, item_index):
#         if item_index > len(self.collection)-1 or item_index < 0:
#             return -1
#         else:
#             if item_index+1 % self.items == 0:
#                 return (item_index+1) / self.items-1
#             else:
#                 if self.items != 1:
#                     return int(str((item_index / self.items))[0])
#                 else:
#                     return int(item_index / self.items)

# Codewars Solution
class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return -(self._item_count // -self.items_per_page)

    def page_item_count(self, page_index):
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1

helper = PaginationHelper(['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q'], 1)
print(helper.page_count())
print(helper.item_count())
print(helper.page_item_count(-1))
print(helper.page_index(12))
