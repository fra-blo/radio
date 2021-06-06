/* Le logiciel permet de savoir à quelle position sont les sélecteurs:
   - de choix du type d'entrée audio (web radio, bluetooth ou jack). Sélecteur à 3 positions
   - de sélection des différentes radios. Sélecteur à 6 positions
   - de sélection des différentes langues pour les radios. Sélecteur à 5 positions
   - de contrôle de volume. Potentiomètre où 5V = volume bas et 0V = volume haut

    Pour les sélecteurs multiposition, un scan type clavier matriciel est effectué.
    Pour ce faire, sur chaque sélecteur, la pin commune est reliée à une résistance de 10k qui est elle-meme connectée à GND.
    Entre la pin commune et la résistance est connecté un fil s'en allant sur une entrée ADC. Dans le logiciel la tension de ces entrées ADC
    s'appellent selec_type_entree, selec_radio, selec_langue.
    Voici la séquence de détection:
    - application de 5V sur la sortie "position 1"
    - lecture des tensions selec_type_entree, selec_radio, selec_langue
    - 3 cas: tension = 0V - le sélecteur pas sur position 1. tension = 5V - sélecteur sur position 1. 
      (pour les selecteur avec + de 3 positions) tension = 2.5V - sélecteur sur la position 4
    - si 2.5 ou 5v, envoi de la position du sélecteur
    - application de 5V sur la sortie "position 2"
    - lecture des tensions selec_type_entree, selec_radio, selec_langue
    - 3 cas tension = 0V - le sélecteur pas sur position 2. tension = 5V - sélecteur sur position 2. 
      (pour les selecteur avec + de 3 positions) tension = 2.5V - sélecteur sur la position 5
    - si 2.5 ou 5v, envoi de la position du sélecteur
     - application de 5V sur la sortie "position 3"
    - lecture des tensions selec_type_entree, selec_radio, selec_langue
    - 3 cas: tension = 0V - le sélecteur pas sur position 3. tension = 5V - sélecteur sur position 3. 
      (pour les selecteur avec + de 3 positions) tension = 2.5V - sélecteur sur la position 6
    - si 2.5 ou 5v, envoi de la position du sélecteur
    
*/

int position1 = 0;
int position2 = 1;
int position3 = 2;

int position_courante = 0;

int selec_type_entree = 0;
int selec_radio = 0;
int selec_langue = 0;
int volume_musique = 0;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(position1, OUTPUT);
  pinMode(position2, OUTPUT);
  pinMode(position3, OUTPUT);
  digitalWrite(position1, LOW);
  digitalWrite(position2, LOW);
  digitalWrite(position3, LOW);
}

// the loop routine runs over and over again forever:
void loop() {
// position 1
  digitalWrite(position3, LOW);
  digitalWrite(position1, HIGH);    
  delay(500);
  selec_type_entree = analogRead(A0);
  selec_radio = analogRead(A1);
  selec_langue = analogRead(A2);

  if (selec_type_entree > 0){
    Serial.print("type ");
    Serial.println(1);
  }
  if (selec_radio > 0){
    Serial.print("radio ");
    if (selec_radio > 768){
      Serial.println(4);
    }
    else{
      Serial.println(1);
    }
  }
  if (selec_langue > 0){
    Serial.print("lan ");
    if (selec_radio > 768){
      Serial.println(4);
    }
    else{
      Serial.println(1);
    }
  }

// position 2
  digitalWrite(position1, LOW);
  digitalWrite(position2, HIGH);    
  delay(500);
  selec_type_entree = analogRead(A0);
  selec_radio = analogRead(A1);
  selec_langue = analogRead(A2);

  if (selec_type_entree > 0){
    Serial.print("type ");
    Serial.println(2);
  }
  if (selec_radio > 0){
    Serial.print("radio ");
    if (selec_radio > 768){
      Serial.println(5);
    }
    else{
      Serial.println(2);
    }
  }
  if (selec_langue > 0){
    Serial.print("lan ");
    if (selec_radio > 768){
      Serial.println(5);
    }
    else{
      Serial.println(2);
    }
  }

// position 3
  digitalWrite(position2, LOW);
  digitalWrite(position3, HIGH);    
  delay(500);
  selec_type_entree = analogRead(A0);
  selec_radio = analogRead(A1);
  selec_langue = analogRead(A2);

  if (selec_type_entree > 0){
    Serial.print("typ ");
    Serial.println(3);
  }
  if (selec_radio > 0){
    Serial.print("rad ");
    if (selec_radio > 768){
      Serial.println(6);
    }
    else{
      Serial.println(3);
    }
  }
  if (selec_langue > 0){
    Serial.print("lan ");
    Serial.println(3);
  }

// volume musique
  volume_musique = analogRead(A3);
  Serial.print("vol ");
  Serial.println(volume_musique);
  
}
