board=[0,1,2,3,4,5,6,7,8]
def showboard():
    print(board[0],"|",board[1],"|",board[2])
    print("---------")
    print (board[3],"|",board[4],"|",board[5])
    print("---------")
    print (board[6],"|",board[7],"|",board[8])
showboard()
counter=0
while counter<5:
    z=int(0)
    for z in range (0,50):
        x=int(input('player 1 its your turn'))
        if(x<0 or x>8):
            print("wrong position")
            x=int(input('player 1 its your turn'))
        else :
            break
    c=int(0)
    for c in range (0,50):
        if board[x]=='x' or board[x]=='o':
                print("taken position")
                x=int(input('player 1 its your turn'))
        
        else :
                board[x]='x'
                showboard()
                break
    if (board[0]=='x' and board[1]=='x' and board[2]=='x'):
        print('player 1 wins')
        break
    elif (board[3]=='x' and board[4]=='x' and board[5]=='x'):
        print('player 1 wins')
        break
    elif (board[6]=='x' and board[7]=='x' and board[8]=='x'):
        print('player 1 wins')
        break
                    
    elif (board[0]=='x' and board[3]=='x' and board[6]=='x'):
        print('player 1 wins')
        break
                        
    elif (board[1]=='x' and board[4]=='x' and board[7]=='x'):
                                print('player 1 wins')
                                break
    elif (board[2]=='x' and board[5]=='x' and board[8]=='x'):
                                       print('player 1 wins')
                                       break
    elif (board[0]=='x' and board[4]=='x' and board[8]=='x'):
                                             print('player 1 wins')
                                             break
    elif (board[2]=='x' and board[4]=='x' and board[6]=='x'):
                                                    print('player 1 wins')
                                                    break                
    if counter == 4 :
        print ("draw")
        break
    c=int(0)
    for c in range (0,50):
        x=int(input("player 2 its your turn"))
        if board[x]=='x' or board[x]=='o':
                print("taken position")
                x=int(input('player 2 its your turn'))
        
        else :
                board[x]='o'
                showboard()
                break
    if (board[0]=='o' and board[1]=='o' and board[2]=='o'):
        print('player 2 wins')
        break
    elif (board[3]=='o' and board[4]=='o' and board[5]=='o'):
        print('player 2 wins')
        break
    elif (board[6]=='o' and board[7]=='o' and board[8]=='o'):
        print('player 2 wins')
        break
    elif (board[0]=='o' and board[3]=='o' and board[6]=='o'):
        print('player 2 wins')
        break
    elif (board[1]=='o' and board[4]=='o' and board[7]=='o'):
        print('player 2 wins')
        break
    elif (board[2]=='o' and board[5]=='o' and board[8]=='o'):
        print('player 2 wins')
        break
    elif (board[0]=='o' and board[4]=='o' and board[8]=='o'):
         print('player 2 wins')
         break
    elif (board[2]=='o' and board[4]=='o' and board[6]=='o'):
         print('player 2 wins')
         break
    counter=counter+1    

        
            
        
    
    
        

        
        
        
    
                                                   
                                             
                       
         
               
        
    
        
    
    
    
    
    
    
    
    

            
      
    
