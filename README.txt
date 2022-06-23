# Licenta

  Lucrarea de fată are ca scop realizarea unui dispozitiv fiabil, capabil să monitorizeze acțiunile motorii pe care utilizatorul le realizează și să detecteze când acesta are sănătatea pusă în pericol din cauza unei căzături.  Deasemenea, ne dorim ca dispozitivul să fie capabil să recunoască ce acțiune realizează utilizatorul, utilizând o metodă de învățare automată pentru a putea clasifica natura acestei activități. Dispozitivul este capabil să detecteze acțiuni din 4 clase:
            1. Staționare
            2. Mers Normal
            3. Alergare
            4. Cădere  
  Pentru a face această acțiune dispozitivul se folosește de un senzor LSM6DS33 care funcționează ca și accelerometru și giroscop pentru detecția înclinației și a accelerației cu care se deplasează utilizatorul, precum și un microcontroler STM32F10 și un modul Bluetooth HC-05 pentru transmiterea datelor către calculator.
  Pentru realizarea detecției acțiunii, a fost implementat și un model de învățare automată alcătuit dintr-o rețea neuronală cu 3 straturi ascunse. Algoritmul prezintă o acuratețe de ~96% în momentul antrenării și ~93% în momentul testării.
  Pentru a putea clasifica în timp real acțiunea realizată de către utilizator, algoritmul folosește un buffer care trebuie să fie calibrat la inițializarea procesului de monitorizare. Rolul acestui buffer este de a crește precizia predicților precum și de a asigura un număr constant de date din fiecare clasă.
