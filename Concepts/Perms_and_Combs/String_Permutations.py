"""
@author: David Lei
@since: 22/08/2016
@modified: 

Java coe
package Algo_Ds_Practice.Permutations;

/**
 * Created by David on 14/04/2016.
 * Time: 2:04 AM
 */

public class Permutations {


    public static void main(String[] args) {

        permuteStart("12");

    }

    public static void permuteStart ( String str ) {
        permute( str.toCharArray(), 0, str.length()-1 ); }

    public static void permute( char [] str, int low, int high ) {
        if ( low == high ) {
            String a = new String(str);
            System.out.println(a);
        }
        else {
            char tmp = str[ low ];
            for ( int i = low; i <= high; i++ ) {
                str[ low ] = str[ i ];
                str[ i ] = tmp;
                permute( str, low+1, high );
                str[ i ] = str[ low ];
            }
            str[ low ] = tmp; }
    }
}

"""
"""
@author: David Lei
@since: 14/06/2016
@modified:

"""

def permutations(string):
    if len(string)<=1:          # base case
        return string
    # perms = permutations(- first char)
    perms = permutations(string[1:])

    char = string[0]            # first char
    result = []
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return resultƒ
print(permutations("abc"))


