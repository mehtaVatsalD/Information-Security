#include <iostream>
#include <string.h>
using namespace std;

int initialHash[64] = {58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7};
int finalHash[64] = {40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25};
int paritydrop[56] = {64,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4};
int compressiontable[48] = {14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32};
string allkeys[16];

string initialpermutation(string plaintext) {
	int i=0,j=0;
	for(i=0;i<64;i++) {
		plaintext[i] = plaintext[initialHash[j]-1];
		j++;
	}
	return plaintext;
}

string finalpermutation(string plaintext) {
	int i=0,j=0;
	for(i=0;i<64;i++) {
		plaintext[i] = plaintext[finalHash[j]-1];
		j++;
	}
	return plaintext;
}

string dropparity(string key) {
	int i=0,j=0;
	string key1;
	for(i=0;i<56;i++) {
		key1 += key[paritydrop[j]-1];
		j++;
	}
	return key1;
}

string keygenerate(string key,int round) {
	string left,right,new_key;
	int i,j=0;
	left = key.substr(0,28);
	right = key.substr(28,55);
	if(round==1 || round==2 || round==9 || round==16) {
		//shift left by 1...
		left = left.substr(1,27) + left[0];
		right = right.substr(1,27) + right[0];
		key = left + right;
	}
	else {
		//shift left by 2...
		left = left.substr(2,27) + left[0] + left[1];
		right = right.substr(2,27) + right[0] + right[1];
		key = left + right;
	}
	// now compress the key...
	for (i=0;i<48;i++) {
		new_key += key[compressiontable[j]-1];
		j++;
	}
	return new_key + key;
}

void generatekey(string key) {
	string temp;
	int i=0;
	//perform parity drop...64 to 56...
	key = dropparity(key);
	//now key has became length of 56...
	for (i=0;i<16;i++) {
		temp = keygenerate(key,i+1);
		allkeys[i] = temp.substr(0,48);
		key = temp.substr(48,103);
	}
}

string rounds(string plaintext,string key) {
	string left,right,new_str;
	left = plaintext.substr(0,32);
	right = plaintext.substr(32,65);
	new_str = des_func(right,key);
	
}

string des(string plaintext,string key) {
	int i;
	//perform initial permutation...
	plaintext = initialpermutation(plaintext);
	//key generation...
	generatekey(key);
	//perform rounds...
	for (i=0;i<16;i++) {
		plaintext = rounds(plaintext,allkeys[i]);	
	}
	//perform final permutation...
	//plaintext = finalpermutation(plaintext);
	return plaintext;
}

int main() {
	string plain,cipher,key;
	plain = "00000001001000110100010101100111100010011010101111001101111011BA";
	key = "000100110011010001010111011110011001101110111100110111111111000A";
	cipher = des(plain,key);
	cout << "The Ciphertext is : " << cipher;
	return 0;
}
