import chess
import random

class ChessAI:
    def __init__(self):
        self.board = chess.Board()

    def evaluate_board(self):
        # Basit bir değerlendirme fonksiyonu
        if self.board.is_checkmate():
            if self.board.turn:
                return -9999  # Siyah kazandı
            else:
                return 9999  # Beyaz kazandı
        # Taşların puan değerlerini hesapla
        wp = len(self.board.pieces(chess.PAWN, chess.WHITE))
        bp = len(self.board.pieces(chess.PAWN, chess.BLACK))
        wn = len(self.board.pieces(chess.KNIGHT, chess.WHITE))
        bn = len(self.board.pieces(chess.KNIGHT, chess.BLACK))
        wb = len(self.board.pieces(chess.BISHOP, chess.WHITE))
        bb = len(self.board.pieces(chess.BISHOP, chess.BLACK))
        wr = len(self.board.pieces(chess.ROOK, chess.WHITE))
        br = len(self.board.pieces(chess.ROOK, chess.BLACK))
        wq = len(self.board.pieces(chess.QUEEN, chess.WHITE))
        bq = len(self.board.pieces(chess.QUEEN, chess.BLACK))
        
        material = 100*(wp-bp) + 320*(wn-bn) + 330*(wb-bb) + 500*(wr-br) + 900*(wq-bq)
        return material

    def minimax(self, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.board.is_game_over():
            return self.evaluate_board()

        if maximizing_player:
            max_eval = -float('inf')
            for move in self.board.legal_moves:
                self.board.push(move)
                eval = self.minimax(depth - 1, alpha, beta, False)
                self.board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.board.legal_moves:
                self.board.push(move)
                eval = self.minimax(depth - 1, alpha, beta, True)
                self.board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_best_move(self, depth=3):
        best_move = None
        best_value = -float('inf')
        alpha = -float('inf')
        beta = float('inf')

        for move in self.board.legal_moves:
            self.board.push(move)
            board_value = self.minimax(depth - 1, alpha, beta, False)
            self.board.pop()
            if board_value > best_value:
                best_value = board_value
                best_move = move

        return best_move

    def play_game(self):
        while not self.board.is_game_over():
            best_move = self.get_best_move()
            if best_move:
                self.board.push(best_move)
                print("Yapılan hamle:", best_move)
                print(self.board)
            else:
                break

        print("Oyun sonuçları:", self.board.result())

# Oyunu başlat
ai_game = ChessAI()
ai_game.play_game()
