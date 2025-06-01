from scapy.all import sniff
def packet_callback(packet):
    return packet.summary()

def format_sniffer_output(packet_summaries):
    formatted_output = ""
    for summary in packet_summaries:
        words = summary.split()  # Split the summary into words
        new_summary = "\n".join([" ".join(words[i:i+3]) for i in range(0, len(words), 3)])  # ✅ Insert newline every 3 words
        formatted_output += new_summary + "\n\n"  # Add extra space between entries
    return formatted_output

def sniff_packets():
    try:
        packets = sniff(count=10, timeout=5)
        summaries = [pkt.summary() for pkt in packets]
        return format_sniffer_output(summaries)  # ✅ Call formatting function
    except Exception as e:
        return f"Error during sniffing: {str(e)}"

    

