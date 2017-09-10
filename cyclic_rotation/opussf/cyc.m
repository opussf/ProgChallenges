// cyc.m

#import <Foundation/Foundation.h>

NSMutableArray * solution( NSMutableArray *A, int K );

int main(int argc, char const *argv[]) {
	NSMutableArray *array = [ NSMutableArray arrayWithCapacity:1 ];

	[ array addObject:@3 ];  // 0?
	[ array addObject:@8 ];  // 1
	[ array addObject:@9 ];  // 2
	[ array addObject:@7 ];  // 3
	[ array addObject:@6 ];  // 4

	NSLog( @"%@", array );

	NSMutableArray *result = solution( array, 3 );

	NSLog( @"%@", result );
	return 0;
}

NSMutableArray * solution( NSMutableArray *A, int K ) {
	for( int lcv = 1; lcv <= K; lcv++ ) {
		id val = [ [ A lastObject ] retain ];        // retain
		[ A removeLastObject ];                      // remove
		[ A insertObject:val atIndex:0 ];
		[ val release ];                             // release
		NSLog( @"%i", lcv );
	}
	return A;
}
