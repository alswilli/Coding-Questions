class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # count = 0
        locals = []
        domains = []
        
        for email in emails:
            for index, char in enumerate(email):
                if char == "@":
                    locals.append(email[0:index])
                    domains.append(email[index:])
                    continue
        
        valids = set()
        
        for index, localname in enumerate(locals):
            # localname = local
            localname = localname.split("+")[0]
            localname = localname.replace(".","")
            localname = (localname + "@" +  domains[index])
            valids.add(localname)
        
        return len(valids)