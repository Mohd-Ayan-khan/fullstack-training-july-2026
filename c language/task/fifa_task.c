#include <stdio.h>

void fifamenu()
{
    printf("\n<||*******####################################################******************||>");
    printf("\n<||>########### FIFA WORLD CUP PLAYER INFORMATION ###########<||>");
    printf("\n<||*******####################################################******************||>");
    printf("\n1. Add Player");
    printf("\n2. See Information");
    printf("\n3. Exit");
    printf("\n<||**********************************************************||>\n");
}

int main()
{
    int number[4];
    char name[4][50];
    char country[4][50];

    int option;
    int dataAdded = 0;

    while (1)
    {
        fifamenu();

        printf("Choose any option: ");
        scanf("%d", &option);

        switch (option)
        {
        case 1:
            printf("\n===== Enter Player Details =====\n");

            for (int i = 0; i < 4; i++)
            {
                printf("\nPlayer %d\n", i + 1);

                printf("Enter Player ID: ");
                scanf("%d", &number[i]);

                printf("Enter Player Name: ");
                scanf("%49s", name[i]);

                printf("Enter Player Country: ");
                scanf("%49s", country[i]);
            }

            dataAdded = 1;
            printf("\nPlayer information saved successfully!\n");
            break;

        case 2:
            if (dataAdded == 0)
            {
                printf("\nNo player information available!\n");
                printf("Please add player details first.\n");
                break;
            }

            printf("\n===== Player Information =====\n");

            for (int i = 0; i < 4; i++)
            {
                printf("\n********************************");
                printf("\nPlayer ID      : %d", number[i]);
                printf("\nPlayer Name    : %s", name[i]);
                printf("\nPlayer Country : %s", country[i]);
                printf("\n********************************\n");
            }
            break;

        case 3:
            printf("\nExiting Program...\n");
            return 0;

        default:
            printf("\nInvalid option! Please try again.\n");
        }
    }

    return 0;
}