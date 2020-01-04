class Box{
    public:
        int getInterior(){
            return interior -> data;
        }
        void setInterior(int data){
            setInteriorH(interior, data);
        }
                struct IntW{
            int data;
        };
    private:
        void setInteriorH(IntW* interior, int dat){
            interior -> data = dat
        }


        IntW* interior;
}

int main(){
    Box thing;
    thing.setInterior(5);
    cout << thing.getInterior();
}