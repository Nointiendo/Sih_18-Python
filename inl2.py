#1/usr/bin/python3
import argparse


parser = argparse.ArgumentParser(description="This tool will extract the string from input file and convert the content into uppercases in outputfile")         #Här ska jag vara ärlig att erkänna att jag inte har full koll på argparse, mycket google.
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")                                                           #optional, ej "mandatory" att använda detta alternativet


RequiredArguments = parser.add_argument_group("Required Arguments")
RequiredArguments.add_argument("-i","--input", type=str, help="Please input the name of the input file", default="input.txt", required=True)              #Mandatory, det vill säga båda 2 filerna krävs för att scriptet skall kunna köras. 
RequiredArguments.add_argument("-o", "--output", type=str, help="Please input the name of the output file", default="output.txt", required=True)

args = parser.parse_args()

inp = args.input                                            #inp blir en variabel för args.input. likaså blir out en variabel för args.output
out = args.output

def read_content():
    try:
        with open(inp, "r") as result:                 #Gillar with statements.Tycker det ger kort och smidig kod samt att de ger en bra output.Ett plus är att filen automatiskt stängs ned med with statements.
            y = result.read().upper()                          #Konverterar om de små bokstäverna från "input.txt" till stora bokstäver och skrivs slutligen in i "output.txt".
        with open(out, "w+") as result2:                #Öppnar filen för att skriva och läsa. Finns ej filen så skapas den.
            result2.write(y)
    except IOError:                                         #IOError, som står för Input Output. Kan uppstå exempelvis när en fil skall öppnas. Filen kanske inte finns eller filen kan ej öppnas av någon annan anledning.
            print("Sorry, we could not find the file")
    except EOFError as eof:                                 #EOFError, som står för End of File. Kan uppstå när data inte läses in korrekt. 
        print("Error, something went wrong with the file")
    except OSError as err:
        print("Sorry, we could not find the file")          #OSError, vad jag kan förstå är det inte någon större skillnad gentemot IOError och OSError.

    finally:
        print("Script is done")

read_content()