import json
import numpy as np
import math

def process_data(data):
    with open('vistemp/attentions.json', 'w') as outfile:
        json.dump(data, outfile)


def process_transformer_data(encoder_self_attention,decoder_self_attention,decoder_encoder_attention):
    encoder_self_list=[]
    for item in encoder_self_attention:
        tmp_dict=item
        tmp_dict["upper_sentence"]=item["source_sentence"]
        tmp_dict["lower_sentence"]=item["source_sentence"]

        for l in range(int(item["num_layer"])):
            tmp_array=np.zeros(np.array(tmp_dict["layer_0-head_0"]).shape)
            for h in range(int(item["num_head"])):
                key="layer_"+str(l)+"-head_"+str(h)
                tmp_array=np.add(tmp_array,np.array(tmp_dict[key]))
            tmp_array=tmp_array/int(item["num_head"])
            tmp_dict["layer_"+str(l)+"-head_avg"]=tmp_array.tolist()
        
        encoder_self_list.append(tmp_dict)
    with open("vistemp/encoder_self_attention.json",'w') as outfile:
        json.dump(encoder_self_list,outfile)
    
    decoder_self_list=[]
    for item in decoder_self_attention:
        tmp_dict=item
        tmp_dict["upper_sentence"]=item["target_sentence"]
        tmp_dict["lower_sentence"]=item["target_sentence"]

        for l in range(int(item["num_layer"])):
            tmp_array=np.zeros(np.array(tmp_dict["layer_0-head_0"]).shape)
            for h in range(int(item["num_head"])):
                key="layer_"+str(l)+"-head_"+str(h)
                tmp_array=np.add(tmp_array,np.array(tmp_dict[key]))
            tmp_array=tmp_array/int(item["num_head"])
            tmp_dict["layer_"+str(l)+"-head_avg"]=tmp_array.tolist()
        
        decoder_self_list.append(tmp_dict)
    with open("vistemp/decoder_self_attention.json",'w') as outfile:
        json.dump(decoder_self_list,outfile)
    

    decoder_encoder_list=[]
    for item in decoder_encoder_attention:
        tmp_dict=item
        tmp_dict["upper_sentence"]=item["source_sentence"]
        tmp_dict["lower_sentence"]=item["target_sentence"]
        I=len(item["source_sentence"])
        J=len(item["target_sentence"])

        to_avg=[]
        for l in range(int(item["num_layer"])):
            tmp_array=np.zeros(np.array(tmp_dict["layer_0-head_0"]).shape)
            for h in range(int(item["num_head"])):
                key="layer_"+str(l)+"-head_"+str(h)
                tmp_array=np.add(tmp_array,np.array(tmp_dict[key]))
                to_avg.append(tmp_dict[key])
            tmp_array=tmp_array/int(item["num_head"])
            tmp_dict["layer_"+str(l)+"-head_avg"]=tmp_array.tolist()
        avg=np.average(np.array(to_avg),axis=0)

        CDP_sum=0
        AP_out=0
        for i in range(I):
            tmp_sum=0
            for j in range(J):
                tmp_sum+avg[i][j]
                AP_out=AP_out+(-1*avg[i][j]*math.log2(avg[i][j]))
            CDP_sum+=math.log2((1-tmp_sum)**2+1)
        CDP_sum=-(CDP_sum)/J
        AP_out=AP_out/I
        confidence=CDP_sum+AP_out
        tmp_dict["confidence"]=confidence


        decoder_encoder_list.append(tmp_dict)
    with open("vistemp/decoder_encoder_attention.json",'w') as outfile:
        json.dump(decoder_encoder_list,outfile)
