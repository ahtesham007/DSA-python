def findminpages(books, s):
    l = min(books)
    h = sum(books)

    while l <= h:
        mid = (l+h)>>1

        def isPossible(mid):
            sc = 1
            pages = 0
            for page in books:
                if pages + page > mid:
                    sc += 1
                    pages = page
                    if pages > mid:
                        return False
                else:
                    pages += page
            
            if sc > s:
                return False
            else:
                return True

        if isPossible(mid):
            h = mid - 1
        else:
            l = mid + 1
        
    return l
    
    

print(findminpages([5, 17, 100, 11], 4))
