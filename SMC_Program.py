# Thomas Nyckel, 2025
# Revised version 1.1

""" For instructions on how to use the program, see the Instructions.md file on GitHub. """
""" For a brief introduction to the purpose and functionalities of the program, see the README.md file in GitHub. """

""" Um mit Zufallszahlen operieren zu können, benötigen wir das Modul random """
import random


# --- INITIALISIERUNG ---
# ----------------------


""" Länge der n-Gramme, die maximal beachtet werden, um aus ihnen den nächsten Buchstaben abzuleiten. """
Länge_der_n_Gramme = 1

""" Bestimmt, wieviele Zeichen lang der neu generierte Text sein soll. """
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

""" Text für die Warnung, die ausgegeben wird, wenn der Input-Text kürzer ist als die Länge der gewünschten
n-Gramme. Das Programm wird dann nicht ausgeführt, da es in diesem Fall abstürzen würde. """
Warnung_Länge = "WARNUNG! Programm konnte nicht ausgeführt werden. Der Input-Text muss ein Zeichen länger sein als die Länge der gewünschten n-Gramme.\n"


# --- ANALYSE ---
# ---------------


""" Ein Abstandhalter wird ausgegeben, um die Ausgabe in der Konsole übersichtlicher zu machen. """
print("\n===============\n")

""" Hier wird Text aus der Datei 'input.txt' geladen, in einzelne Zeichen zerlegt und in einer Liste gespeichert. """

""" Textfile 'input.txt' öffnen und seinen Inhalt einlesen. """
with open('input.txt','r', encoding="utf-8") as text_file: # Öffnen der Datei
	file_contents = text_file.read() # Speichern des Inhalts der Datei in file_contents

""" Nun werden die n-Gramme werden aus dem Input-Text gelesen und im dict abgelegt. Dies beinhaltet noch keine
Übergangswahrscheinlichkeiten bzw. die auf die n-Gramme folgenden Zeichen. Diese werden in einem späteren Schritt
extra analysiert und gespeichert. """

""" Vorgehen:
Damit wir uns an der Länge_der_n_Gramme orientieren können, ohne diesen Wert zu überschreiben, speichern wir den
Wert aus Länge_der_n_Gramme in der neuen Variable nGrammlänge_in_Schleife.
Ist der Input-Text kürzer als Länge_der_n_Gramme? Falls ja, Abbruch mit Hinweis.
Erste Hauptschleife, nGrammlänge_in_Schleife wird dekrementiert bis 0.
Zeichenfolgen mit nGrammlänge_in_Schleife, nGrammlänge_in_Schleife -1, etc. Länge werden als keys im dict abgelegt.
Im Dictionary wird ein key angelegt für jede Zeichenfolge bis zur Länge nGrammlänge_in_Schleife aus dem Input.
Damit werden alle n-Gramme aus dem Input-text im Dictionary gespeichert.
Redundante Zeichen werden nicht beachtet. Die jeweils letzten Zeichenfolgen aus dem Input-Text werden nicht angehängt,
da hierfür kein folgendes Zeichen mehr vorliegt und im nächsten Schritt keine Übergangswahrscheinlichkeit
bestimmt werden kann. Dies könnte sonst zu einem out of bounds error führen. Es muss daher hier - 1 abgezogen werden.
um das letzte Zeichen des Texts nicht mit auszulesen. """

""" Diese Variable wird in der Schleife genutzt, um alle n-Gramme durchzugehen. """
nGrammlänge_in_Schleife = Länge_der_n_Gramme

""" Zu Länge_der_n_Gramme wird hier 1 addiert. Dies verhindert, dass der gesamte Input als ein n-Gramm herangezogen wird.
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
		""" Nachdem alle n-Gramme mit der maximal vorgegebenen Länge gespeichert sind, wird 1 von nGrammlänge_in_Schleife
  		abgezogen. Daher werden im nächsten Durchlaufe die nächstkleineren n-Gramme gespeichert. """
		nGrammlänge_in_Schleife = nGrammlänge_in_Schleife - 1

""" Die auf die n-Gramme jeweils folgenden Zeichen werden in die als values des dicts fungierenden listen abgelegt. """

""" Das Programm geht die n-Gramme von nGrammlänge_in_Schleife bis 1 durch und zieht das auf diese jeweils folgende
Zeichen aus dem Input-Text. Die letzte Zeichenfolge wird jeweils ausgelassen, da auf dieses kein weiteres Zeichen mehr
folgt und das Programm sonst out of bounds gehen würde. Da oftmals mehrere values einem gemeinsamen key zugewiesen werden
müssen – dies ist der Fall, da auf ein und dieselbe Zeichenfolge verschiedene andere Zeichen an unterschiedlichen Stellen
des Texts folgen können –, werden diese in Listen im Dictionary gespeichert. Diese Listen können später direkt verwendet
werden, um im Syntheseteil random Zeichen aus ihnen zu ziehen. Da in jedem Schritt immer auch das nächstfolgende Zeichen
angesteuert wird in Zeichen_aus_Text, muss - 1 in der ersten Schleife abgezogen werden. Sonst ginge das Programm über den
Umfang der Liste hinaus und würde eine Fehlermeldung produzieren. """

""" Diese Variable wird erneut in der Schleife genutzt, um alle n-Gramme durchzugehen. """
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
			Zeichen aus dem Input in der Liste als value im dict gespeichert wird. """
			Übergangswahrscheinlichkeiten[Zeichenfolge_aus_Text].append(file_contents[index + nGrammlänge_in_Schleife])
		nGrammlänge_in_Schleife = nGrammlänge_in_Schleife - 1

print(f"Analyseteil abgeschlossen\n")

# --- SYNTHESE ---
# ----------------

""" Der Syntheseteil besteht aus zwei neuen Modulen:

Erstes Modul: Anfangsroutine

Da zuerst kein Output vorliegt, aus dem Länge_der_n_Gramme Zeichen oder weniger geholt werden könnten, muss zuerst
Output bis zur Länge Länge_der_n_Gramme erzeugt werden. Diese Anfangsroutine holt erst zufällig ein Zeichen aus dem
dafür vorgesehenen Anfangsalphabet (das nicht gleich dem zufälligen Alphabet ist) und sucht dann sukzessive nach der
jeweils schon als Output vorliegenden Zeichenfolge im dict, bis die Länge des Outputs gleich Länge_der_n_Gramme ist. """

""" Der erste Buchstabe des Outputs wird random aus den Großbuchstaben gezogen. """
Ausgabestring = Ausgabestring + (random.choice(Alphabet_Großbuchstaben))

""" Zu Länge_der_n_Gramme wird 1 addiert. Dies verhindert, dass der gesamte Input als ein n-Gramm herangezogen wird.
In diesem Fall gäbe es sonst kein Zeichen als value für diesen key und damit käme es zu einem error. """
if len(file_contents) >= Länge_der_n_Gramme + 1:
	""" Der Anfangsteil des Ausgabestrings wird zusammengesetzt. Der Anfangsteil des Ausgabestrings muss so lange sein wie
 	Länge_der_n_Gramme, dann kann nach dieser Funktion die Hauptroutine der Analyse starten. """
	for Länge_Ausgabe_dynamisch in range (1, Länge_der_n_Gramme):
		""" Beginnend mit der vollen Länge des Ausgabestrings wird immer wieder um 1 dekrementiert bis 0 erreicht ist.
		Das macht es möglich, immer kleinere Zeichenfolgen vom Ende des Ausgabestrings her zu betrachten, wenn notwendig. """
		for Länge_betrachtete_Zeichenfolge in range(Länge_Ausgabe_dynamisch, -1, -1):
			""" Wurde auch das letzte Zeichen des Outputs nicht gefunden als Key im dict, wird zufällig ein nächstes Zeichen
			bestimmt. """
			if Länge_betrachtete_Zeichenfolge == 0:
				""" Wurde kein match im dict gefunden, auch nicht für das letzte Zeichen des Ausgabestrings, so
				wird random ein Zeichen aus dem Alphabet für Kleinbuchstaben gezogen. """
				Nächstes_Zeichen = (random.choice(Alphabet_Kleinbuchstaben))
				""" Da ein nächstes Zeichen für den Ausgabestring gefunden wurde, wird die innere for-Schleife abgebrochen. """
				break
			else:
				""" Geprüft wird, ob die jeweils letzten Zeichen des Outputs ein key im dict sind. Sind sie es, wird zufällig
				ein nächstes Zeichen aus dem dazugehörigen value gezogen. """
				if Ausgabestring[ -(Länge_betrachtete_Zeichenfolge):] in Übergangswahrscheinlichkeiten:
					""" Gab es ein match im dict, wird das nächste Zeichen random aus der zum key gehörigen Liste (die das value
	 				zu diesem key bildet) gezogen. """
					Nächstes_Zeichen = random.choice(Übergangswahrscheinlichkeiten[Ausgabestring[ - (Länge_betrachtete_Zeichenfolge):]])
					""" Da ein nächstes Zeichen nun gefunden wurde, wird die innere for-Schleife abgebrochen. """
					break
		""" Das zuvor bestimmte Zeichen wird an das Ende des Outputs angefügt. """
		Ausgabestring = Ausgabestring + Nächstes_Zeichen

""" Zweites Modul: Hauptteil der Synthesefunktion

Die eigentliche Synthese sucht nun im dict nach keys identisch zu den letzten Länge_der_n_Gramme Zeichen des bereits
bestehenden Outputs. Gibt es kein match, sucht es nach den letzten Länge_der_n_Gramme - 1 Zeichen, etc.,
bis Länge_der_n_Gramme = 1. Wird auch hier nichts gefunden, wird ein zufälliges Zeichen gezogen.

Der Output wird dann ausgegeben. """

""" Zu Länge_der_n_Gramme wird 1 addiert. Dies verhindert, dass der gesamte Input als ein n-Gramm herangezogen wird.
In diesem Fall gäbe es sonst kein Zeichen als value für diesen key und damit käme es zu einem error. """
if len(file_contents) >= Länge_der_n_Gramme + 1:
	""" Solange die gewünschte Zeichenzahl im Ausgabestring nicht erreicht wurde, sollen weitere Zeichen gezogen werden. """
	while len(Ausgabestring) < laenge_Ausgabe:
		""" Die letzten Zeichen des Ausgabestrings werden betrachtet. Beginnend bei der in Länge_der_n_Gramme
		festgesetzten Länge an Zeichen. Diese Länge wird dann, wenn notwendig, im weiteren Verlauf verkürzt. """
		for Länge_betrachtete_Zeichenfolge in range (Länge_der_n_Gramme, -1, -1):
			if Länge_betrachtete_Zeichenfolge == 0:
				""" Wurde kein Match im dict gefunden, auch nicht für das letzte Zeichen des Ausgabestrings, so
				wird random ein Zeichen aus dem Alphabet für Kleinbuchstaben gezogen. """
				Nächstes_Zeichen = (random.choice(Alphabet_Kleinbuchstaben))
				""" Die folgende Zeile kann aktiviert werden zum Debugging durch Entfernen der Raute. """
				# print(f"Nächstes_Zeichen = {Nächstes_Zeichen}. Random.")
				""" Da ein nächstes Zeichen nun gefunden wurde, wird die innere for-Schleife abgebrochen. """
				break
			else:
				""" Geprüft wird, ob die jeweils letzten Zeichen des Outputs ein key im dict sind. Sind sie es, wird zufällig
				ein nächstes Zeichen aus dem dazugehörigen value gezogen. """
				if Ausgabestring[ -(Länge_betrachtete_Zeichenfolge):] in Übergangswahrscheinlichkeiten:
					""" Gab es ein match im dict, wird das nächste Zeichen random aus der zum key gehörigen Liste als value
					gezogen. """
					Nächstes_Zeichen = random.choice(Übergangswahrscheinlichkeiten[Ausgabestring[ - (Länge_betrachtete_Zeichenfolge):]])
					""" Kann aktiviert werden zum Debugging durch Entfernen der Raute. """
					# print(f"Nächstes_Zeichen = {Nächstes_Zeichen}. Aus Dict Key: {Ausgabestring[ - (Länge_betrachtete_Zeichenfolge):]}")
					""" Da ein nächstes Zeichen nun gefunden wurde, wird die innere for-Schleife abgebrochen. """
					break
		""" Das zuvor bestimmte Zeichen wird an das Ende des Outputs angefügt. """
		Ausgabestring = Ausgabestring + Nächstes_Zeichen
		""" Kann aktiviert werden zum Debugging durch Entfernen der Raute. """
		# print(Ausgabestring)

""" Kann durch Entfernen der Raute aktiviert werden, um zum Debugging den Inhalt des dicts Übergangswahrscheinlichkeiten
auszugeben. """
# print(f"Übergangswahrscheinlichkeiten: {Übergangswahrscheinlichkeiten}")

""" Werte zur Ansicht ausgeben. """
print(f"Länge_der_n_Gramme = {Länge_der_n_Gramme}")
print(f"laenge_Ausgabe = {laenge_Ausgabe}\n")

""" Ausgabestring als zentrales Ergebnis des Programms ausgeben. """
""" Dies aber nur, wenn auch etwas erzeugt wurde, wenn also der Input-text um 1 länger war als die gewünschte Länge
der n-Gramme. War das nicht der Fall, wird stattdessen ausgegeben, wie lang der Input-text war. """
if len(file_contents) >= Länge_der_n_Gramme + 1:
	print(f'Generierter Text:\n\n"{Ausgabestring}"\n')
else:
	print(f"Die Länge des Input-Texts war zu kurz, nämlich nur {len(file_contents)} Zeichen lang.\nDer Input-Text muss ein Zeichen länger sein als Länge_der_n_Gramme.\n")
