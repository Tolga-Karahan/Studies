import "fmt"

func lengthOfLongestSubstring(s string) int {
    dict := make(map[string]struct{})
    var longest string

    for i:=0; i<len(s)-1; i++ {
        longest = string(s[i])
        dict[longest] = struct{} {}
        for j:=i+1; j<len(s); j++ {
            next := string(s[j])
            _, ok := dict[next]
            if !ok  {
                dict[next] = struct{} {}
                longest = longest + next
            } 
        }   
        dict = make(map[string]struct{})
    }

    fmt.Println(longest)
    return len(longest)
}
