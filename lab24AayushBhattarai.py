import secrets

# Fake "encryption" function: just reverses the string + key for demo
def simple_encrypt(key, msg):
    return (msg[::-1] + key)  # reverse string + key

def simple_decrypt(key, msg):
    return msg.replace(key, "")[::-1]  # remove key, reverse back

def kerberos_sim_simple():
    print("--- Simple Kerberos Simulation ---\n")
    
    # Step 0: Shared long-term secrets
    K_client = "CLIENTKEY"
    K_server = "SERVERKEY"
    
    # Step 1: Client requests TGT
    Na = secrets.token_hex(4)  # Client nonce
    print(f"Step 1: Client -> AS: Request TGT, Nonce={Na}")
    
    # Step 2: AS generates TGT and session key
    Ks = secrets.token_hex(8)  # Session key
    TGT = simple_encrypt(K_server, Ks + ",Client")
    print(f"Step 2: AS -> Client: TGT (encrypted with server key) & Session Key (Ks={Ks})")
    
    # Step 3: Client sends TGT to TGS for service ticket
    print(f"Step 3: Client -> TGS: Send TGT to request Service Ticket")
    ST = simple_encrypt(K_server, Ks + ",AppServer")
    print(f"Step 3: TGS -> Client: Service Ticket (ST) generated")
    
    # Step 4: Client presents ST to Application Server
    print(f"Step 4: Client -> AppServer: Present ST for access")
    decrypted_ST = simple_decrypt(K_server, ST)
    print(f"         AppServer decrypted ST: {decrypted_ST}")
    
    # Step 5: Server challenge (nonce)
    Nb = secrets.token_hex(4)
    print(f"Step 5: AppServer -> Client: Challenge with Nonce={Nb}")
    # Client responds using session key (fake encryption)
    response = simple_encrypt(Ks, Nb)
    print(f"Step 6: Client -> AppServer: Response={response}")
    
    # Step 6: Server verifies
    verified_Nb = simple_decrypt(Ks, response)
    if verified_Nb == Nb:
        print("\nAuthentication SUCCESS! Client can access resources.")
    else:
        print("\nAuthentication FAILED!")

# Run simulation
kerberos_sim_simple()