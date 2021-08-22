load high.dat;
load lat.dat;
load lon.dat;

%%
fid=fopen('hgt.bin', 'w')
fwrite(fid, high, 'double')
fclose(fid);

fid=fopen('lat.bin', 'w')
fwrite(fid, lat, 'double')
fclose(fid);

fid=fopen('lon.bin', 'w')
fwrite(fid, lon, 'double')
fclose(fid);

%%
fileID = fopen('hgt.bin');
bhgt = fread(fileID,[1913 1006],'double');

fileID = fopen('lat.bin');
blat = fread(fileID,[1913 1006],'double');

fileID = fopen('lon.bin');
blon = fread(fileID,[1913 1006],'double');

index=[-1 1];
pcolor(blon, blat, bhgt)
shading interp
hold on
contour(blon,blat, bhgt, index,'-k'); 
axis equal; 
%axis([118.5 123.5 20.5 26.5])
%colormap(gray(128));
%test(128:-1:1,:)=colormap;
%colormap(test);
colorbar





