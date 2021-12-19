const double pi =TMath::Pi(); 
double fit_func(double *x,double *par){
        return par[0] / pow(sin((x[0]-par[1])*pi/360),4);
}

void ruther_ford(){
 gStyle->SetOptFit(1111);
 gStyle->SetOptStat(111111);
 TCanvas *c1=new TCanvas("me","A graph",500,500,500,500);
 c1->SetLogy(1);
 TGraph *g1=new TGraph("gold_5mm.txt");

 TF1 *f3=new TF1("f3",fit_func,-30,30,2);
 
 f3->SetLineColor(kBlack);
 f3->SetParNames("A","B");
 g1->Fit("f3","R");
 //g1->SetDrawOption(2);
 g1->SetMarkerStyle(33);
 g1->SetTitle("Gold Foil in 5mm slit;#theta in degree;N(#theta)");
 TLegend *leg=new TLegend(0.1,0.8,0.3,0.9,"My Legend");
 leg->AddEntry(g1,"Data Points","p");
 leg->AddEntry("f3","Fitting Line","l");
 


 g1->Draw("APE");
 f3->Draw("Same");
 leg->Draw("Same");
}
