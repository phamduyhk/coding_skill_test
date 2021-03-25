#include <stdio.h>

// 盤の初期化関数
void init_board(int board[3][3])
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            board[i][j] = 0;
        }
    }
}

// 盤の表示関数
void print_board(int board[3][3])
{
    int i, j;
    printf(" --- --- --- \n");
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            printf("|");
            if (board[i][j] == 0)
                printf("   ");
            else if (board[i][j] == 1) //1は○プレイヤー
                printf(" O ");
            else if (board[i][j] == -1) //-1はxプレイヤー
                printf(" X ");
        }
        printf("|\n");
        printf(" --- --- --- \n");
    }
}
// 盤の更新関数
// 盤の(x,y)マスをplayerの入力と更新する
void update_board(int board[3][3], int x, int y, int player)
{
    board[x][y] = player;
}

//各プレイヤーのての入力
void player_input(int board[3][3], int player)
{
    int x, y;

    if (player == 1)
    {
        printf("Oのターンです\n");
    }
    else
    {
        printf("Xのターンです\n");
    }
    do
    {
        do
        {
            printf("行の位置(0～2)は？");
            scanf("%d", &x);
        } while (x < 0 || x > 2);
        do
        { //◆
            printf("列の位置(0～2)は？");
            scanf("%d", &y);
        } while (y < 0 || y > 2);
    } while (board[x][y] != 0);

    //　盤の更新
    update_board(board, x, y, player);
}

// 勝ち負け判定関数
int judge(int board[3][3])
{
    int x, y; //xは行の位置、yは列の位置
    for (x = 0; x < 3; x++)
    {
        if (board[0][x] != 0)
        {
            if (board[0][x] == board[1][x] && board[1][x] == board[2][x])
            {
                return board[0][x]; // x行に三つ揃って、勝ちプレイヤーを返す（1か-1か）
            }
        }
    }
    for (y = 0; y < 3; y++)
    {
        if (board[y][0] != 0)
        {
            if (board[y][0] == board[y][1] && board[y][1] == board[y][2])
            {
                return board[y][0]; // y列に三つ揃って、勝ちプレイヤーを返す（1か-1か）
            }
        }
    }
    if (board[1][1] != 0)
    {
        if (board[0][0] == board[1][1] && board[1][1] == board[2][2])
        {
            return board[1][1]; //斜めに三つ揃って、勝ちプレイヤーを返す（1か-1か）
        }
        if (board[0][2] == board[1][1] && board[1][1] == board[2][0])
        {
            return board[1][1]; //斜めに三つ揃って、勝ちプレイヤーを返す（1か-1か）
        }
    }
    for (x = 0; x < 3; x++)
    {
        for (y = 0; y < 3; y++)
        {
            if (board[y][x] == 0)
            {
                return 0; //勝ち負けまだ判明していないので0を返す
            }
        }
    }
    return 2; //引き分け
}

// 結果報告関数
void print_result(int result)
{
    if (result == 1)
        printf("0の勝ちです\n");
    else if (result == -1)
        printf("Xの勝ちです\n");
    else
        printf("引き分けです\n");
}

int main(void)
{
    // 盤の初期化
    int board[3][3];
    init_board(board);
    int player = 1; // 1は○プレイヤー,-1はxプレイヤー
    int result;

    // 勝ち負けが判定されるまでゲームを続ける
    while ((result = judge(board)) == 0)
    {
        print_board(board);
        player_input(board, player);
        //　次のプレイヤーのターン
        player *= -1;
    }
    print_board(board);
    print_result(result);

    return 0;
}