# Thomas Nyckel, 2025
# Revised version 1.1

""" For instructions on how to use the program, see the Instructions.md file on GitHub. """

""" Um mit Zufallszahlen operieren zu können, benötigen wir das Modul random """
import random


# --- INITIALISIERUNG ---
# ----------------------


""" Länge der n-Gramme, die maximal beachtet werden, um aus ihnen den nächsten Buchstaben abzuleiten """
Länge_der_n_Gramme = 4

""" Bestimmt, wieviele Zeichen lang der neu generierte Text sein soll """
laenge_Ausgabe = 500

""" Ein Alphabet von Großbuchstaben, die dann random gezogen werden können. """
Alphabet_Großbuchstaben = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
	'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

""" Ein Alphabet von Kleinbuchstaben, die dann random gezogen werden können. """
Alphabet_Kleinbuchstaben = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
	'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

""" Speichert später implizit die Übergangswahrscheinlichkeiten zwischen aufeinanderfolgenden Zeichenfolgen und Buchstaben. """
Übergangswahrscheinlichkeiten = {}

""" Dieser String enhält am Ende den Output des Programms. """
Ausgabestring = ''

""" Text für die Warnung, die ausgegeben wird, wenn der Input-Text kürzer ist als die Länger der gewünschten
n-Gramme. Das Programm wird dann nicht ausgeführt, da es in diesem Fall abstürzen würde. """
Warnung_Länge = "WARNUNG! Programm konnte nicht ausgeführt werden. Der Input-Text muss ein Zeichen länger sein als die Länge der gewünschten n-Gramme.\n"


# --- ANALYSE ---
# ---------------


""" Ein Abstandhalter für die Übersichtlichkeit der Ausgabe wird ausgegeben. """
print("\n===============\n")

""" Hier wird Text aus der Datei 'test-file.txt' geladen, in einzelne Zeichen zerlegt und in einer Liste gespeichert """

""" Textfile öffnen und einlesen """
with open('input.txt','r', encoding="utf-8") as text_file: # Öffnen der Datei
	file_contents = text_file.read() # Lesen der Datei

# Die n-Gramme werden aus dem Input-Text gelesen und im dict abgelegt.

""" Ist der Input-Text kürzer als n? Falls ja, Abbruch mit Hinweis.
Erste Hauptschleife, n wird dekrementiert bis 0.
Zeichenfolgen mit n, n -1, etc. Länge werden als keys im dict abgelegt.
Im Dictionary wird ein Key angelegt für jede Zeichenfolge bis zur Länge n aus dem Input.
Redundante Zeichen werden nicht beachtet. Die jeweils letzten Zeichenfolgen aus dem Input-Text werden nicht angehängt,
da hierfür kein folgendes Zeichen mehr vorliegt und im nächsten Schritt keine Übergangswahrscheinlichkeit
bestimmt werden kann. Dies könnte sonst zu einem out of bounds führen. Es muss daher hier - 1 abgezogen werden.
um das letzte Zeichen des Texts nicht mit auszulesen. """

""" Diese Variable wird in der Schleife genutzt, um alle n-Gramme durchzugehen. """
nGrammlänge_in_Schleife = Länge_der_n_Gramme

""" Zu Länge_der_n_Gramme wird 1 addiert. Dies verhindert, dass der gesamte Input als ein n-Gramm herangezogen wird.
In diesem Fall gäbe es sonst kein Zeichen als value für diesen key und damit käme es zu einem error. """
if len(file_contents) < Länge_der_n_Gramme + 1:
	print(Warnung_Länge)
else:
	while nGrammlänge_in_Schleife > 0:
		""" eigentlich müsste von nGrammlänge_in_Schleife - 1 abgezogen werden, um den gesamten Input in keys zu
		überführen. Da die jeweils letzte Zeichenfolge aber ausgelassen werden muss, um einen error zu vermeiden,
		der entsteht, da auf diese Folgen kein Zeichen mehr folgen kann und diese keys daher ein leeres value hätten,
		wird auf dieses - 1 verzichtet. """
		for index in range(len(file_contents) - (nGrammlänge_in_Schleife)):
			Zeichenfolge_aus_Text = file_contents[index:index + nGrammlänge_in_Schleife]
			Übergangswahrscheinlichkeiten[Zeichenfolge_aus_Text] = []
		""" Nachdem alle n-Gramme gespeichert sind, wird 1 davon abgezogen und die dann im nächsten Durchlauf die
		nächstkleineren n-Gramme gespeichert. """
		nGrammlänge_in_Schleife = nGrammlänge_in_Schleife - 1

# Die auf die n-Gramme jeweils folgenden Zeichen werden in die als values des dicts fungierenden listen abgelegt.

""" Das Programm die n-Gramme von n bis 1 durch und zieht das auf diese jeweils folgende Zeichen aus dem Input-Text
Die letzte Zeichenfolge wird jeweils ausgelassen, da auf dieses kein weiteres Zeichen mehr folgt und das Programm
sonst out of bounds gehen würde. Da oftmals mehrere Values einem gemeinsamen key zugewiesen werden müssen – da auf
ein und dieselbe Zeichenfolge verschiedene andere Zeichen an unterschiedlichen Stellen des Texts folgen können –,
werden diese in einer Liste im Dictionary gespeichert. Diese Liste kann später direkt verwendet werden, um im
Syntheseteil random Zeichen aus ihr zu ziehen. Da in jedem Schritt immer auch das nächstfolgende Zeichen angesteuert
wird in Zeichen_aus_Text, muss - 1 in der ersten Schleife abgezogen werden. Sonst ginge das Programm über den Umfang
der Liste hinaus und würde eine Fehlermeldung produzieren. """

""" Diese Variable wird in der Schleife genutzt, um alle n-Gramme durchzugehen. """
nGrammlänge_in_Schleife = Länge_der_n_Gramme

""" Zu Länge_der_n_Gramme wird 1 addiert. Dies verhindert, dass der gesamte Input als ein n-Gramm herangezogen wird.
In diesem Fall gäbe es sonst kein Zeichen als value für diesen key und damit käme es zu einem error. """
if len(file_contents) >= Länge_der_n_Gramme + 1:
	while nGrammlänge_in_Schleife > 0:
		""" eigentlich müsste von nGrammlänge_in_Schleife - 1 abgezogen werden, um den gesamten Input in keys zu
		überführen. Da die jeweils letzte Zeichenfolge aber ausgelassen werden muss, um einen error zu vermeiden,
		der entsteht, da auf diese Folgen kein Zeichen mehr folgen kann und diese keys daher ein leeres value hätten,
		wird auf dieses - 1 verzichtet. """
		for index in range(len(file_contents) - (nGrammlänge_in_Schleife)):
			Zeichenfolge_aus_Text = file_contents[index:index + nGrammlänge_in_Schleife]
			""" index + nGrammlänge_in_Schleife + 1 bedeutet, dass das auf die Zeichenfolge jeweils direkt folgende
			Zeichen aus dem Input in der Liste als Value im dict gespeichert wird. """
			Übergangswahrscheinlichkeiten[Zeichenfolge_aus_Text].append(file_contents[index + nGrammlänge_in_Schleife])
		nGrammlänge_in_Schleife = nGrammlänge_in_Schleife - 1

print(f"Analyseteil abgeschlossen\n")

# --- SYNTHESE ---
# ----------------

""" Der Syntheseteil besteht aus zwei neuen Modulen:

Erstes Modul: Anfangsroutine

Da zuerst kein Output vorliegt, aus dem _n_ Zeichen oder weniger geholt werden könnten, muss zuerst Output bis zur
Länge n erzeugt werden. Diese Anfangsroutine holt erst zufällig ein Zeichen aus dem dafür vorgesehenen
Anfangsalphabet (das nicht gleich dem zufälligen Alphabet ist) und sucht dann sukzessiv nach der jeweils schon als
Output vorliegenden Zeichenfolge im dict, bis die Länge des Outputs gleich n ist. """

""" Der erste Buchstabe des Outputs wird random aus den Großbuchstaben gezogen. """
Ausgabestring = Ausgabestring + (random.choice(Alphabet_Großbuchstaben))

""" Zu Länge_der_n_Gramme wird 1 addiert. Dies verhindert, dass der gesamte Input als ein n-Gramm herangezogen wird.
In diesem Fall gäbe es sonst kein Zeichen als value für diesen key und damit käme es zu einem error. """
if len(file_contents) >= Länge_der_n_Gramme + 1:
	""" Der Anfangsteil des Ausgabestrings wird zusammengesetzt """
	""" Der Anfangsteil des Ausgabestrings muss so lange sein wie Länge_der_n_Gramme, dann kann nach dieser Funktion die
	Hauptroutine der Analyse starten. """
	for Länge_Ausgabe_dynamisch in range (1, Länge_der_n_Gramme):
		""" Beginnend mit der vollen Länge des Ausgabestrings wird immer wieder um 1 dekrementiert bis 0.
		Das macht es möglich, immer kleinere Zeichenfolgen vom Endes Ausgabestrings zu betrachten, wenn notwendig. """
		for Länge_betrachtete_Zeichenfolge in range(Länge_Ausgabe_dynamisch, -1, -1):
			""" wurde auch das letzte Zeichen des Outputs nicht gefunden als Key im dict, wird zufällig ein nächstes Zeichen
			bestimmt. """
			if Länge_betrachtete_Zeichenfolge == 0:
				""" Wurde kein Match im dict gefunden, auch nicht für das letzte Zeichen des Ausgabestrings, so
				wird random ein Zeichen aus dem Alphabet für Kleinbuchstaben gezogen. """
				Nächstes_Zeichen = (random.choice(Alphabet_Kleinbuchstaben))
				""" Da ein nächstes Zeichen nun gefunden wurde, wird die innere for Schleife unterbrochen. """
				break
			else:
				""" Geprüft wird, ob die jeweils letzten Zeichen des Outputs ein key im dict sind. Sind sie es, wir zufällig
				ein nächstes Zeichen aus dem dazugehörigen value gezogen. """
				""" Die jeweils letzten Zeichen des Ausgabestrings werden herangezogen und geprüft, ob sie ein key
				im dict der Übergangswahrscheinlichkeiten sind. """
				if Ausgabestring[ -(Länge_betrachtete_Zeichenfolge):] in Übergangswahrscheinlichkeiten:
					""" Gab es ein match im dict, wird das nächste Zeichen random aus der zum key gehörigen Liste als value
					gezogen. """
					Nächstes_Zeichen = random.choice(Übergangswahrscheinlichkeiten[Ausgabestring[ - (Länge_betrachtete_Zeichenfolge):]])
					""" Da ein nächstes Zeichen nun gefunden wurde, wird die innere for Schleife unterbrochen. """
					break
		""" Das zuvor bestimmte Zeichen oder die Zeichenfolge wird an das Ende des Outputs angefügt. """
		Ausgabestring = Ausgabestring + Nächstes_Zeichen

""" Zweites Modul: Hauptteils der Synthesefunktion

Die eigentliche Synthese sucht dann im dict nach keys identisch zu den letzten n Zeichen des bereits bestehenden
Outputs. Gibt es kein match, sucht es nach den letzten n-1 Zeichen, etc., bis n = 1. Wird auch hier nichts gefunden,
wird ein zufälliges Zeichen gezogen.

Der Output wird dann ausgegeben. """

""" Zu Länge_der_n_Gramme wird 1 addiert. Dies verhindert, dass der gesamte Input als ein n-Gramm herangezogen wird.
In diesem Fall gäbe es sonst kein Zeichen als value für diesen key und damit käme es zu einem error. """
if len(file_contents) >= Länge_der_n_Gramme + 1:
	""" Solange die gewünschte Zeichenzahl im Ausgabestring nicht erreicht wurde, sollen dann weitere Zeichen
	gezogen werden. """
	while len(Ausgabestring) < laenge_Ausgabe:
		""" Die letzten Zeichen des Ausgabestrings werden betrachtet. Beginnend bei der in Länge_der_n_Gramme
		festgesetzten Länge an Zeichen. Diese Länge wird dann ggf. im weiteren Verlauf verkürzt. """
		for Länge_betrachtete_Zeichenfolge in range (Länge_der_n_Gramme, -1, -1):
			if Länge_betrachtete_Zeichenfolge == 0:
				""" Wurde kein Match im dict gefunden, auch nicht für das letzte Zeichen des Ausgabestrings, so
				wird random ein Zeichen aus dem Alphabet für Kleinbuchstaben gezogen. """
				Nächstes_Zeichen = (random.choice(Alphabet_Kleinbuchstaben))
				""" Kann aktiviert werden zum Debugging. """
				# print(f"Nächstes_Zeichen = {Nächstes_Zeichen}. Random.")
				""" Da ein nächstes Zeichen nun gefunden wurde, wird die innere for Schleife unterbrochen. """
				break
			else:
				""" Geprüft wird, ob die jeweils letzten Zeichen des Outputs ein key im dict sind. Sind sie es, wir zufällig
				ein nächstes Zeichen aus dem dazugehörigen value gezogen. """
				""" Die jeweils letzten Zeichen des Ausgabestrings werden herangezogen und geprüft, ob sie ein key
				im dict der Übergangswahrscheinlichkeiten sind. """
				if Ausgabestring[ -(Länge_betrachtete_Zeichenfolge):] in Übergangswahrscheinlichkeiten:
					""" Gab es ein match im dict, wird das nächste Zeichen random aus der zum key gehörigen Liste als value
					gezogen. """
					Nächstes_Zeichen = random.choice(Übergangswahrscheinlichkeiten[Ausgabestring[ - (Länge_betrachtete_Zeichenfolge):]])
					""" Kann aktiviert werden zum Debugging. """
					# print(f"Nächstes_Zeichen = {Nächstes_Zeichen}. Aus Dict Key: {Ausgabestring[ - (Länge_betrachtete_Zeichenfolge):]}")
					""" Da ein nächstes Zeichen nun gefunden wurde, wird die innere for Schleife unterbrochen. """
					break
		""" Das zuvor bestimmte Zeichen oder die Zeichenfolge wird an das Ende des Outputs angefügt. """
		Ausgabestring = Ausgabestring + Nächstes_Zeichen
		""" Kann aktiviert werden zum Debugging. """
		# print(Ausgabestring)

""" Kann aktiviert werden, um zum Debugging den Inhalt des Dicts Übergangswahrscheinlichkeiten auszugeben. """
# print(f"Übergangswahrscheinlichkeiten: {Übergangswahrscheinlichkeiten}")

""" Werte zur Ansicht ausgeben. """
print(f"Länge_der_n_Gramme = {Länge_der_n_Gramme}")
print(f"laenge_Ausgabe = {laenge_Ausgabe}\n")

""" Ausgabestring als zentrales Ergebnis des Programms ausgeben. """
""" Dies aber nur, wenn auch etwas erzeugt wurde, wenn also der Input-Text eins länger war als die gewünschte Länge
der n-Gramme. War das nicht der Fall, wird stattdessen ausgegeben, wie lang der Input-Text war. """
if len(file_contents) >= Länge_der_n_Gramme + 1:
	print(f'Generierter Text:\n\n"{Ausgabestring}"\n')
else:
	print(f"Die Länge des Input-Texts war zu kurz, nämlich nur {len(file_contents)} Zeichen lang.\nDer Input-Text muss ein Zeichen länger sein als Länge_der_n_Gramme.\n")
