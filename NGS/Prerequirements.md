# Pre-required packages

In order to process our sequences, we will need to have some programs installed in our Linux system.

We are going to need the FASTX toolkit. You can install it following these commands:

```
cd /usr/local/src/

sudo wget https://github.com/agordon/libgtextutils/releases/download/0.7/libgtextutils-0.7.tar.gz

sudo tar -xzf libgtextutils-0.7.tar.gz

cd libgtextutils-0.7

sudo sed -i '47s/input_stream/static_cast<bool>(input_stream)/' src/gtextutils/text_line_reader.cpp

sudo ./configure

sudo make

sudo make install

cd ../

sudo wget https://github.com/agordon/fastx_toolkit/releases/download/0.0.14/fastx_toolkit-0.0.14.tar.bz2

sudo tar -xjf fastx_toolkit-0.0.14.tar.bz2

cd fastx_toolkit-0.0.14

sudo wget https://github.com/agordon/fastx_toolkit/files/1182724/fastx-toolkit-gcc7-patch.txt

sudo patch -p1 < fastx-toolkit-gcc7-patch.txt

sudo ./configure

sudo make

sudo make install

cd ../
```

We will also need PEAR. You need to “purchase” it (it’s free for users in academia!) here:

`https://www.h-its.org/downloads/pear-academic/`

They will send you a download link. Then you need to place the downloaded file in your Linux system, and run these commands, but **remember to modify them** to use the real folder where you place your PEAR installation file and the actual version that you downloaded:

```
cd /usr/local/src/

sudo cp ~/pear-0.9.11-linux-x86_64.tar.gz ./

sudo tar -xzf pear-0.9.11-linux-x86_64.tar.gz

cd pear-0.9.11-linux-x86_64

sudo cp bin/pear /usr/local/bin/

sudo gzip man/pear.1

sudo cp man/pear.1.gz /usr/share/man/man1/
```

Another software that we will need is BLAST and its associated programs. We can install it running the following commands, replacing [BLAST_VERSION] for the numbers of the last version of the software (you can check which ones are available going to `ftp.ncbi.nlm.nih.gov/blast/executables/blast+/` in your Internet browser.

```
cd /usr/local/src/

sudo wget "ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/[BLAST_VERSION]/ncbi-blast-[BLAST_VERSION]+-x64-linux.tar.gz"

sudo tar -zxf ncbi-blast-[BLAST_VERSION]+-x64-linux.tar.gz

sudo cp ncbi-blast-[BLAST_VERSION]+/bin/* /usr/local/bin/
```

And finally we will install FASTQC, which is straightforward:

```
cd /usr/local/src/

sudo wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.9.zip

sudo unzip fastqc_v0.11.9.zip

sudo chmod a+x FastQC/fastqc

sudo ln -s /usr/local/src/FastQC/fastqc /usr/local/bin/fastqc
```

We will also need to be sure that we have Python 3 installed in our Linux system.

```
sudo apt-get install python3
```

And we have to install CROP, which needs to be compiled from the source:

```
cd /usr/local/src

sudo git clone https://github.com/tingchenlab/CROP

sudo make
```

