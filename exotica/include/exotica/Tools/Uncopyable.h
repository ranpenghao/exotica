#ifndef UNCOPYABLE_H
#define UNCOPYABLE_H

namespace exotica
{
class Uncopyable
{
public:
    Uncopyable() {}
    ~Uncopyable() {}
private:
    Uncopyable(const Uncopyable&);
    Uncopyable& operator=(const Uncopyable&);
};
}

#endif  // UNCOPYABLE_H
