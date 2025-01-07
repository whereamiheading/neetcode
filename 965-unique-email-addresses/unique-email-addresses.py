class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emails_set = set()

        for email in emails:
            partial , domain = email.split('@')[0],  email.split('@')[-1]
            e = partial.split('+')[0].replace('.', '') + '@' + domain
            emails_set.add(e)
        return len(emails_set)