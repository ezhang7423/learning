// You can edit this code!
// Click here and start typing.
package main

import "fmt"

func main() {
	unsorted := []int{9, 7, 6, 3, 2, 1, -1}
	for i := 0; i < len(unsorted); i++ {
		j := i;
		
			for unsorted[j] > unsorted[j+1] {
				tmp := unsorted[j];
				unsorted[j] = unsorted[j+1]
				unsorted[j+1] = tmp;	
				if j == len(unsorted) - 1 {
					break;
				} else {
					j++;
				}
			}
		}
	fmt.Println(unsorted)

}
