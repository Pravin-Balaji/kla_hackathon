import math

def matching_pairs(lengths_poi,lengths_source):
    p = []
    for i in range(len(lengths_poi)):
        for j in range(len(lengths_source)):
            print(len(lengths_poi[i]),len(lengths_source[j]))
            if len(lengths_source[i]) == len(lengths_poi[j]) and lengths_poi[i][0]//lengths_source[j][0] == lengths_poi[i][1]//lengths_source[j][1] == lengths_poi[i][2]//lengths_source[j][2] == lengths_poi[i][3]//lengths_source[j][3] == lengths_poi[i][4]//lengths_source[j][4] == lengths_poi[i][5]//lengths_source[j][5]:
                pass
            else:
                p.append(lengths_source[j])
    return p

def distances(poi,source):
    lengths_source = []
    lengths_poi = []

    for i in range(len(poi)):
        if poi[i] == 'boundary\n' and 'xy' in poi[i+3]:
            poi_xy = poi[i+3].split(" ")
            poi_xy = [ele for ele in poi_xy if ele.strip()]
            y = 0
            a1 = []
            while 2 + y < 2 * int(poi_xy[1]) - 1:
                u1 = (int(poi_xy[2 + y]) - int(poi_xy[4 + y])) * (int(poi_xy[2 + y]) - int(poi_xy[4 + y]))
                v1 = (int(poi_xy[3 + y]) - int(poi_xy[5 + y])) * (int(poi_xy[3 + y]) - int(poi_xy[5 + y]))
                a1 += [math.sqrt(u1 + v1)]
                y += 2
            a1.sort()
            lengths_poi.append(a1)
    for j in range(len(source)):
        a = []
        if source[j] == 'boundary\n' and 'xy' in source[j+3]:
            source_xy = source[j+3].split(" ")
            source_xy = [ele for ele in source_xy if ele.strip()]
            z = 0
            while 2+z < 2*int(source_xy[1])-1:
                u = (int(source_xy[2+z])-int(source_xy[4+z]))*(int(source_xy[2+z])-int(source_xy[4+z]))
                v = (int(source_xy[3+z])-int(source_xy[5+z]))*(int(source_xy[3+z])-int(source_xy[5+z]))
                a += [math.sqrt(u+v)]
                z += 2
            a.sort()
            lengths_source.append(a)
    return lengths_poi,lengths_source


def output_verification(k):
    output1 = open("output1.txt", "w")
    for i in range(len(k)):
         if k[i] == 'boundary\n':
             if 'layer' in k[i+1] and 'datatype' in k[i+2] and 'xy' in k[i+3] and 'endel' in k[i+4]:
                 output1.write(k[i])
                 output1.write(k[i+1])
                 output1.write(k[i+2])
                 output1.write(k[i+3])
                 output1.write(k[i+4])


if __name__ == '__main__':
    input1 = open("Format_Source.txt", "r")
    k = input1.readlines()
    output_verification(k)
    input2 = open("POI.txt","r")
    input3 = open("Source.txt","r")
    poi = input2.readlines()
    source = input3.readlines()
    lengths_poi,lengths_source = distances(poi,source)
    p = matching_pairs(lengths_poi,lengths_source)
    print(len(p))











