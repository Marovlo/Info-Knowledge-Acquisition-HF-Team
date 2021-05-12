names=[f'E:\\articals\\prose\\{i}.txt'for i in range(1,2564)]

for name in names:
    lines=[]
    ans=[]
    with open(name,'r',encoding='utf-8')as f:
        lines=f.readlines()
        for line in lines:
            if line!="\n":
                line=line.replace('\u3000','')
                line=line.replace('\xa0','')
                ans.append(line)
    with open(name,"w",encoding='utf-8')as f:
        f.writelines(ans)