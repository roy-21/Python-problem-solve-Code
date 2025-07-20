#include <iostream>
using namespace std;

int main()
{
    int n, value, i, pos = 0;
    cout << "List size: ";
    cin >> n;
    int arr[n+1]; 

    cout << "Enter sorted list: ";
    for (i = 0; i < n; i++) 
    {
        cin >> arr[i];
    }
    cout << "Enter value to insert: ";
    cin >> value;

    for (i = 0; i < n; i++) 
    {
        if (arr[i] > value) 
        {
            pos = i;
            break;
        }
    }

    if (i == n) 
    {
        pos = n;
    }

    for (i = n; i > pos; i--)
    {
        arr[i] = arr[i-1];
    }

    arr[pos] = value;

    cout << "Updated list: ";
    for (i = 0; i <= n; i++) 
    {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}