#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    QPushButton *menu;

    ui->setupUi(this);

    connect(menu, &QPushButton::clicked, this, &MainWindow ::on_pushButton_clicked);

//    this->layout = new QVBoxLayout;
//    this->layout->addWidget(button0);

}

MainWindow::~MainWindow()
{
    delete ui;

}

void MainWindow::on_pushButton_clicked()
{
    QPushButton *menu;
    QPushButton *profile = new QPushButton( "&Your Profile", this);
    QPushButton *history = new QPushButton( "&History", this);
    QPushButton *addingr = new QPushButton( "&Add Ingridients", this);
    QPushButton *diet = new QPushButton( "&Diet", this);
    QPushButton *search = new QPushButton( "&Search with filters", this);

    profile->show();
    history->show();
    addingr->show();
    search->show();

//    button0 ->addAction(profile);
//    button0 ->addAction(history);
//    button0 ->addAction(addingr);
//    button0 ->addAction(diet);
//    button0 ->addSeparator();
//    button0 ->addAction(search);

}

