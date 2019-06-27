class Solution {
    public int numUniqueEmails(String[] emails) {
        if (emails == null) {
            return 0;
        }

        Set<String> addresses = new HashSet<>();
	  
        for (String email : emails) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < email.length(); i++) {
                char ch = email.charAt(i);
                switch (ch) {
                    case '.':
                        break;
                    case '+':
                        while (ch != '@') {
                            i++;
                            ch = email.charAt(i);
                        }
                        sb.append(email.substring(i));
                        i = email.length();
                    break;
                    case '@':
                        sb.append(email.substring(i));
                        i = email.length();
                        break;
                    default:
                        sb.append(ch);
                }
            }
            addresses.add(sb.toString());
        }
        return addresses.size();
    }
} 