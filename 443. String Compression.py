class Solution:
    def compress(self, chars: List[str]) -> int:
        pre = chars[0]
        pos, cnt = 0, 0
        for ch in chars:
            if pre == ch:
                cnt += 1
            else:
                chars[pos] = pre
                pos += 1
                if cnt > 1:
                    cnt = str(cnt)
                    for i in range(len(cnt)):
                        chars[pos] = cnt[i]
                        pos += 1
                pre = ch
                cnt = 1
        chars[pos] = pre
        pos += 1
        
        if cnt > 1:
            cnt = str(cnt)
            for i in range(len(cnt)):
                chars[pos] = cnt[i]
                pos += 1
        return pos
    
   
        
