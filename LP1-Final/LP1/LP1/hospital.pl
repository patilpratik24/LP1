go:-
	h1(Disease),
	write('It is suggested that the patient has '),
	write(Disease),
	nl,
	undo;
	write('Sorry, the system is unable to identify the disease'),
	nl,
	undo.

h1(cold):-
	symptom(headache),
	symptom(runny_nose),
	symptom(sneezing),
	symptom(sore_throat),
	nl,
	write('Advices and suggestions:'),
	nl,
	write('1: Tylenol'),
	nl,
	write('2: Panadol'),
	nl,
	write('3: Nasal Spray'),
	nl,
	write('Please wear warm clothes because'),
	nl,!.

h1(influenza):-
	symptom(sore_throat),
	symptom(fever),
	symptom(headache),
	symptom(chills),
	symptom(body_ache),
	nl,
	write('Advices and suggestions:'),
	nl,
	write('1: Tamiflue'),
	nl,
	write('2: Panadol'),
	nl,
	write('3: Zanamivir'),
	nl,
	write('Please take warm bath and do salt gargaling because'),
	nl,!.

h1(typhoid):-
	symptom(headache),
	symptom(abdominal_pain),
	symptom(poor_appetite),
	symptom(fever),
	nl,
	write('Advices and suggestions:'),
	nl,
	write('1: Chlorsmphenicaol'),
	nl,
	write('2: Amoxicillin'),
	nl,
	write('3: Ciprofloxacin'),
	nl,
	write('4: Azithromycin'),
	nl,
	write('Please take complete bed rest and take soft diet because'),
	nl,!.

h1(chicken_pox):-
	symptom(rash),
	symptom(body_ache),
	symptom(fever),
	nl,
	write('Advices and suggestions:'),
	nl,
	write('1: Varicella'),
	nl,
	write('2: Immunoglobulin'),
	nl,
	write('3: Acyclovir'),
	nl,
	write('Please do have oatmeal and stay at home because'),
	nl,!.


h1(measles):-
	symptom(fever),
	symptom(runny_nose),
	symptom(rash),
	symptom(conjuctivitis),
	nl,
	write('Advices and suggestions:'),
	nl,
	write('1: Tylenol'),
	nl,
	write('2: Aleve'),
	nl,
	write('3: Advil'),
	nl,
	write('4: Viatmin A'),
	nl,
	write('Please get rest and use more liquid because'),
	nl,!.

h1(malaria):-
	symptom(fever),
	symptom(sweaing),
	symptom(headache),
	symptom(nausea),
	symptom(vomiting),
	symptom(diarrhea),
	nl,
	write('Advices and suggestions:'),
	nl,
	write('1: Aralen'),
	nl,
	write('2: Qualaquin'),
	nl,
	write('3: Plaquenil'),
	nl,
	write('4: Mefloquine'),
	nl,
	write('Please do not sleep in open air and cover your full skin because'),
	nl,!.

h1(dengue):-
	symptom(headache),
	symptom(fever),
	symptom(headache),
	symptom(bodypain),
	symptom(vomiting),
	nl,
	write('Advices and suggestions:'),
	nl,
	write('1: ABC'),
	nl,
	write('2: XYZ'),
	nl,
	write('3: PQR'),
	nl,
	write('Please wear warm clothes because'),
	nl,!.

h1(diabetes):-
	symptom(weight_loss),
	symptom(skin_infection),
	symptom(blur_visoin),
	symptom(hunger),
	nl,
	write('Advices and suggestions:'),
	nl,
	write('1: Medicines'),
	nl,
	write('2: abs'),
	nl,
	write('3: asd'),
	nl,
	write('Please avoid sweets because'),
	nl,!.

h1(brain_tumour):-
	symptom(head_ache),
	symptom(sleepiness),
	symptom(fatigue),
	symptom(memory_loss),
	nl,
	write('Advices and suggestions:'),
	nl,
	write('1: sadzd'),
	nl,
	write('2: lsdf'),
	nl,
	write('3: sdgj'),
	nl,
	write('Please visit to hospital because'),
	nl,!.

h1(diarrhea):-
	symptom(lose_motion),
	symptom(dehydration),
	symptom(digestive_problem),
	symptom(vomitting),
	nl,
	write('Advices and suggestions:'),
	nl,
	write('1: sadzd'),
	nl,
	write('2: lsdf'),
	nl,
	write('3: sdgj'),
	nl,
	write('Please keep your body hydrated because'),
	nl,!.

h1(food_poisoning):-
	symptom(vomitting),
	symptom(lose_motion),
	symptom(syomach_pain),
	symptom(bloating),
	nl,
	write('Advices and suggestions:'),
	nl,
	write('1: sadzd'),
	nl,
	write('2: lsdf'),
	nl,
	write('3: sdgj'),
	nl,
	write('Please eat fruits because'),
	nl,!.


ask(Question):-
	write('Does the patient has the symptom '),
	write(Question),
	write('? : '),
	read(Response),
	nl,
	(   (Response==yes ; Response==y)
	->
	assert(yes(Question));
	assert(no(Question)), fail).

:-dynamic yes/1,no/1.

symptom(S):-
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
