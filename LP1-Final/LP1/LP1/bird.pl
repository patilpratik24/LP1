go:-
	h1(Type),
	write('It is suggested that the bird is '),
	write(Type),
	nl,
	undo;
	write('Sorry, the system is unable to identify the bird'),
	nl,
	undo.

h1(sparrow):-
	feature(four_inch_length),
	feature(thick_conical_bill),
	feature(gray_brown_crown),
	nl,!.

h1(kingfisher):-
	feature(nineteen_cm_long),
	feature(large_beak),
	feature(short_tail),
	feature(green_crest),
	feature(long_stout_dark_bill),
	nl,!.

h1(golden_eagle):-
	feature(three_feet),
	feature(two_meter_wingspan),
	feature(dark_yellowish_brown_colour),
	nl,!.

h1(cuckoo):-
	feature(thirty_two_cm_length),
	feature(white_belly_gray_stripes),
	feature(pointed_black_bill),
	feature(seventy_six_cm_wingspan),
	nl,!.

h1(bald_eagle):-
	feature(feathers_on_leg),
	feature(seven_feet_wingspan),
	feature(dark_white_colour_on_head),
	feature(dark_brown_colour),
	nl,!.

ask(Question):-
	write('Does the bird has the feature '),
	write(Question),
	write('? : '),
	read(Response),
	nl,
	(   (Response==yes ; Response==y)
	->
	assert(yes(Question));
	assert(no(Question)), fail).

:-dynamic yes/1,no/1.

feature(S):-
	(   yes(S)
	->
	true;
	(   no(S)
	->
	fail;
	ask(S))).

undo:-
	retract(yes(_)),fail.
undo:-
	retract(no(_)),fail.
undo.















