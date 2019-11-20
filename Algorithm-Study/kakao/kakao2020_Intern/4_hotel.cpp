// def solution(k, room_number):
//     answer = []

//     room = [0] * k

//     for roomNum in room_number :
//         roomNum = roomNum - 1
//         if room[roomNum] == 0 :
//             room[roomNum] = roomNum + 1
//             answer.append(roomNum + 1)

//         else :
//             temp = []
//             temp.append(roomNum)
//             nextIndex = room[roomNum]
//             while room[nextIndex] != 0 :
//                 temp.append(nextIndex)
//                 nextIndex = room[nextIndex]
//             for i in temp :
//                 room[i] = nextIndex + 1
//             room[nextIndex] = nextIndex + 1
//             answer.append(nextIndex + 1)

//     return answer


#include <string>
#include <vector>

using namespace std;

vector<long long> solution(long long k, vector<long long> room_number) {
    vector<long long> answer;
    
    vector<long long> room;
    for (int i = 0; i < k; i ++) {
        room.push_back(0);
    }

    for (long long i : room_number) {
        long long roomNum = i - 1;
        if (room[roomNum] == 0) {
            room[roomNum] = roomNum + 1;
            answer.push_back(roomNum + 1);
        } else {
            vector <long long> temp;
            temp.push_back(roomNum);
            long long nextIndex = room[roomNum];
            while (room[nextIndex] != 0) {
                temp.push_back(nextIndex);
                nextIndex = room[nextIndex];
            }
            for (long long j : temp) {
                room[j] = nextIndex + 1;
            }
            room[nextIndex] = nextIndex + 1;
            answer.push_back(nextIndex + 1);
        }
    }
    
    return answer;
}