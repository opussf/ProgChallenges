// bg.cpp
// binary_gap
// Hey...  my C++ is RUSTY!

#include <stdio.h>
//#include <iostream.h>

int solution( int N );

int main() {
	const int testNum = 9;
	int tests[ testNum * 2 ] = {
			1041, 5,
			1089, 5,
			0, 0,
			20, 1,
			529, 4,
			9, 2,
			8, 0,
			15, 0,
			2147483647, 0,
		 };

	int bitCount;
	for( int lcv = 0; lcv < testNum; lcv++ ) {
		int testVal = tests[ lcv * 2 ];
		int expected = tests[ ( lcv * 2 ) + 1 ];

		bitCount = solution( testVal );
		if( bitCount == expected ) {
			printf( "The binary gap for %i is %i\n", testVal, bitCount );
		} else {
			printf( "The binary gap for %i returned %i, but %i was expected.\n", testVal, bitCount, expected );
		}
	}

	return( 0 );
}

int solution( int N ) {
	int zeroCount = 0;
	int zeroCountMax = 0;
	bool oneSeen = false;

	while( N > 0 ) {
		if( N % 2 ) {
			zeroCountMax = (zeroCount > zeroCountMax) ? zeroCount : zeroCountMax;
			zeroCount = 0;
			oneSeen = true;
		}
		else if( oneSeen ) {
			zeroCount++;
		}
		//printf( "%i\t%i\t%i\t%i\n", bit, zeroCount, zeroCountMax, N );
		N = N >> 1;
	}
	return( zeroCountMax );

}
