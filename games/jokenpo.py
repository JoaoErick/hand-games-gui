from typing import List, Dict
from handtracking import HandDetector

class Jokenpo:
    def __init__(self, hand_detector: HandDetector, hands: List[Dict]) -> None:
        """ Método construtor.
        
        Parameters
        ----------
        hand_detector: :class:`HandDetector`
            Detector de mãos.
        hands: :class:`List`
            Lista contendo as posições dos dedos das mãos
        """
        
        self.hand_detector:HandDetector  = hand_detector
        self.hands: List[Dict] = hands

    def start_game(self) -> str:
        """ Método para decidir o vencedor do jogo Jokenpô.
        
        Returns
        ------
        :class:`str`
        """

        if(len(self.hands) > 0):
            moves: List[int] = []

            for hand in self.hands:
                moves.append(self.__player_move(hand))

            if(len(moves) == 2):
                if(moves[0] == moves[1]):
                    return "Empate!"
                elif(moves[0] == 1 and moves[1] == 2):
                    return "Jogador que jogou PAPEL venceu!"
                elif(moves[0] == 1 and moves[1] == 3):
                    return "Jogador que jogou PEDRA venceu!"
                elif(moves[0] == 2 and moves[1] == 1):
                    return "Jogador que jogou PAPEL venceu!"
                elif(moves[0] == 2 and moves[1] == 3):
                    return "Jogador que jogou TESOURA venceu!"
                elif(moves[0] == 3 and moves[1] == 1):
                    return "Jogador que jogou PEDRA venceu!"
                elif(moves[0] == 3 and moves[1] == 2):
                    return "Jogador que jogou TESOURA venceu!"

    def __player_move(self, hand: List[Dict]) -> int:
        """ Indica qual foi a jogada de um jogador.
        `Pedra -> 1 | Papel -> 2 | Tesoura -> 3`

        Parameters
        ----------
        hand: :class:`List`
            Lista contendo as posições dos dedos de uma mão.

        Returns
        ------
        :class:`int`
        """

        if(self.__is_rock(hand)):
            return 1
        elif(self.__is_paper(hand)):
            return 2
        elif(self.__is_scissors(hand)):
            return 3
        else:
            return -1
    
    def __is_rock(self, hand: List[Dict]) -> bool:
        """ Verifica se o sinal feito com a mão representa a 'pedra' do jogo
        Jokenpô.

        Parameters
        ----------
        hand: :class:`List[Dict]`
            Lista contendo as mãos.

        Returns
        -------
        :class:`bool`
        """

        return True if (
            not self.hand_detector.is_thumb_raised(hand) and
            not self.hand_detector.is_index_finger_raised(hand) and
            not self.hand_detector.is_middle_finger_raised(hand) and
            not self.hand_detector.is_ring_finger_raised(hand) and
            not self.hand_detector.is_pinky_raised(hand)
        ) else False
    
    def __is_paper(self, hand: List[Dict]) -> bool:
        """ Verifica se o sinal feito com a mão representa o 'papel' do jogo
        Jokenpô.

        Parameters
        ----------
        hand: :class:`List`
            Lista contendo as mãos.

        Returns
        -------
        :class:`bool`
        """

        return True if (
            self.hand_detector.is_thumb_raised(hand) and
            self.hand_detector.is_index_finger_raised(hand) and
            self.hand_detector.is_middle_finger_raised(hand) and
            self.hand_detector.is_ring_finger_raised(hand) and
            self.hand_detector.is_pinky_raised(hand)
        ) else False
    
    def __is_scissors(self, hand: List[Dict]) -> bool:
        """ Verifica se o sinal feito com a mão representa a 'tesoura' do jogo
        Jokenpô.

        Parameters
        ----------
        hand: :class:`List`
            Lista contendo as mãos.

        Returns
        -------
        :class:`bool`
        """

        return True if (
            not self.hand_detector.is_thumb_raised(hand) and
            self.hand_detector.is_index_finger_raised(hand) and
            self.hand_detector.is_middle_finger_raised(hand) and
            not self.hand_detector.is_ring_finger_raised(hand) and
            not self.hand_detector.is_pinky_raised(hand)
        ) else False