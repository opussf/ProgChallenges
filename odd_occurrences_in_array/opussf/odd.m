// odd.m
// This is really my first Objective C program.
// Most of writing this was asking the question:
//     "How do I do <bleh> in Objective C?"
// and then:
//     "Well of course, and I wonder what that symbol really means?"
// and:
//     "These []s are getting old in a hurry."

#import <Foundation/Foundation.h>

int solution(NSMutableArray *A);

int main(int argc, char const *argv[]) {
	NSMutableArray *array = [ NSMutableArray arrayWithCapacity:1 ];

	[ array addObject:@9 ];  // 0?
	[ array addObject:@3 ];  // 1
	[ array addObject:@9 ];  // 2
	[ array addObject:@3 ];  // 3
	[ array addObject:@9 ];  // 4
	[ array addObject:@7 ];  // 5
	[ array addObject:@9 ];  // 6

	// NSLog( @"%@", array );

	int unpaired = solution( array );

	NSLog( @"The unpaired value is %i.\n", unpaired );
	return 0;
}

int solution( NSMutableArray *A ) {
	NSMutableDictionary *noPairs = [ [ NSMutableDictionary alloc ] init ];
	for( id element in A ) {
		if( noPairs[element] ) {
			NSLog( @"Found a pair for %@\n", element );
			[ noPairs removeObjectForKey:element ];
		} else {
			NSLog( @"No pair found yet for %@\n", element );
			[ noPairs setValue:@TRUE forKey:element ];
		}
	}
	NSArray *noPairsKeys = [ noPairs allKeys ];

	if( [ noPairsKeys count ] == 1 ) {
		NSLog( @"Found just 1\n" );
		return [ [ noPairsKeys objectAtIndex:0 ] intValue ];
	}
	return 0;
}
