class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_altitude=0
        h_alti = 0
        for i in range(0,len(gain)):
            curr_altitude = curr_altitude + gain[i] 
            if curr_altitude > h_alti:
                h_alti=curr_altitude
            else:
                continue     
        return h_alti
            
           

        