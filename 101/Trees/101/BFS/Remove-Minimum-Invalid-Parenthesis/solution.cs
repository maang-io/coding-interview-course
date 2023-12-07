// https://leetcode.com/problems/remove-invalid-parentheses/
public class Solution
{
    public IList<string> RemoveInvalidParentheses(string s)
    {
        IList<string> result = new List<string>();
        if (string.IsNullOrEmpty(s))
        {
            result.Add(string.Empty);
            return result;
        }
        Queue<string> queue = new Queue<string>();
        HashSet<string> hashSet = new HashSet<string>();
        queue.Enqueue(s);
        hashSet.Add(s);
        while (queue.Count > 0)
        {
            string cur = queue.Dequeue();
            if (IsValid(cur))
            {
                result.Add(cur);
            }
 
            if (result.Count > 0)
            {
                continue;
            }
 
            for (int i = 0; i < cur.Length; ++i)
            {
                if (cur[i] != '(' && cur[i] != ')') // case of any char e.g. a in (a)
                    continue;
                string temp = cur.Remove(i, 1);
                if (!hashSet.Contains(temp))
                {
                    queue.Enqueue(temp);
                    hashSet.Add(temp);
                }
            }
        }
 
        return result;
    }
 
    bool IsValid(string exp)
    {
        int count = 0;
        foreach (char ch in exp)
        {
            if (count < 0)
                return false;
            if (ch == '(')
                ++count;
            else if (ch == ')')
            {
                --count;
            }
        }
        return count == 0;
    }
 
}
