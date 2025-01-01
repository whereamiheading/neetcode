class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        cities = {}
        for item in paths:
            cities[item[0]] = item[1]
        for k,v in cities.items():
            if v not in cities:
                return v