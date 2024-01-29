// Accepted: 96ms (90.64%), 58.15MB (64.39%)

class Node {
public:
    int key;
    int value;
    Node* next;
    Node(int key = 0, int value = 0, Node* next = nullptr) {
        this->key = key;
        this->value = value;
        this->next = next;
    }
};

class MyHashMap {
    static constexpr int SIZE = 2047;
    Node* map[SIZE];

    int getHash(int key) {
        return key % SIZE;
    }
public:
    MyHashMap() {
        for (int i = 0; i < SIZE; ++i) {
            map[i] = new Node();
        }
    }

    void put(int key, int value) {
        int keyHash = getHash(key);
        Node* node = map[keyHash];

        while (node->next != nullptr) {
            if (key == node->next->key) {
                node->next->value = value;
                return;
            }

            node = node->next;
        }

        node->next = new Node(key, value);
    }

    int get(int key) {
        int keyHash = getHash(key);
        Node* node = map[keyHash];

        while (node->next != nullptr) {
            if (key == node->next->key) {
                return node->next->value;
            }

            node = node->next;
        }

        return -1;
    }

    void remove(int key) {
        int keyHash = getHash(key);
        Node* node = map[keyHash];

        while (node->next != nullptr) {
            if (key == node->next->key) {
                node->next = node->next->next;
                return;
            }

            node = node->next;
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
